from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import time
from datetime import datetime
from pathlib import Path
from xml.etree import ElementTree as ET
from zoneinfo import ZoneInfo

from PIL import Image

from adb_common import Adb, TARGET_PACKAGE

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research" / "target-dongzheng-ai"
SENSITIVE = re.compile(
    r"(总资产|总市值|可用资金|可取|参考盈亏|资金持仓|持仓|账户号|资金账号|身份证|手机号|姓名|买入|卖出|撤单|银证转账|当日委托|当日成交|条件单)"
)
SAFE_FINANCE_MARKET = re.compile(r"(涨幅|跌幅|成交额|指数|行业|概念|榜单|最新价)")


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="ignore")).hexdigest()[:16]


def bounds_center(bounds: str) -> tuple[int, int] | None:
    m = re.match(r"\[(\d+),(\d+)\]\[(\d+),(\d+)\]", bounds)
    if not m:
        return None
    x1, y1, x2, y2 = map(int, m.groups())
    return (x1 + x2) // 2, (y1 + y2) // 2


def node_records(root: ET.Element, redact: bool = False) -> list[dict]:
    records = []
    for index, node in enumerate(root.iter("node")):
        text = node.get("text", "").strip()
        desc = node.get("content-desc", "").strip()
        if redact and (SENSITIVE.search(text) or SENSITIVE.search(desc)):
            text = "[已脱敏]" if text else ""
            desc = "[已脱敏]" if desc else ""
        center = bounds_center(node.get("bounds", ""))
        records.append({
            "index": index,
            "class": node.get("class", "").split(".")[-1],
            "clickable": node.get("clickable") == "true",
            "scrollable": node.get("scrollable") == "true",
            "enabled": node.get("enabled") == "true",
            "selected": node.get("selected") == "true",
            "text": text,
            "content_desc": desc,
            "resource_id": node.get("resource-id", ""),
            "bounds": node.get("bounds", ""),
            "center": center,
        })
    return records


def sanitize_xml(root: ET.Element) -> str:
    clone = ET.fromstring(ET.tostring(root, encoding="utf-8"))
    for node in clone.iter("node"):
        for attr in ("text", "content-desc"):
            value = node.get(attr, "")
            if value and SENSITIVE.search(value):
                node.set(attr, "[已脱敏]")
        if node.get("text") and re.fullmatch(r"[\d\s.,%+\-*·]{6,}", node.get("text", "").strip()):
            node.set("text", "[已脱敏]")
    ET.indent(clone)
    return "<?xml version='1.0' encoding='utf-8'?>\n" + ET.tostring(clone, encoding="unicode")


def summary_markdown(label: str, meta: dict, records: list[dict]) -> str:
    lines = [
        f"# {label}",
        "",
        f"- 采集时间：{meta['captured_at']}",
        f"- 前台：`{meta['focus']}`",
        f"- 页面签名：`{meta['signature']}`",
        f"- 敏感模式：`{meta['scope']}`",
        "",
        "## 可交互元素",
        "",
        "| 序号 | 控件 | 文本/描述 | 可点击 | 可滚动 | 中心坐标 | 边界 |",
        "|---:|---|---|---|---|---|---|",
    ]
    for item in records:
        text = (item["text"] or item["content_desc"]).replace("|", "\\|")
        if not text and not item["clickable"] and not item["scrollable"]:
            continue
        lines.append(
            f"| {item['index']} | {item['class']} | {text} | {item['clickable']} | "
            f"{item['scrollable']} | {item['center']} | `{item['bounds']}` |"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--label", required=True)
    parser.add_argument("--scope", choices=["public", "sensitive"], default="public")
    parser.add_argument("--tap-x", type=int)
    parser.add_argument("--tap-y", type=int)
    parser.add_argument("--wait-ms", type=int, default=1500)
    parser.add_argument("--no-bring-front", action="store_true")
    args = parser.parse_args()

    adb = Adb()
    adb.require_device()
    if not args.no_bring_front:
        adb.bring_target_to_front()
    if (args.tap_x is None) != (args.tap_y is None):
        raise SystemExit("--tap-x and --tap-y must be provided together")
    if args.tap_x is not None:
        adb.tap(args.tap_x, args.tap_y)
        time.sleep(args.wait_ms / 1000)

    now = datetime.now(ZoneInfo("Asia/Shanghai"))
    stamp = now.strftime("%Y%m%d_%H%M%S")
    safe_label = re.sub(r"[^0-9A-Za-z_\-\u4e00-\u9fff]+", "_", args.label).strip("_")
    focus = adb.current_focus()
    png = b""
    for attempt in range(3):
        candidate = adb.screenshot_png()
        try:
            with Image.open(io.BytesIO(candidate)) as image:
                image.verify()
            png = candidate
            break
        except Exception:
            time.sleep(0.8)
    if not png:
        raise RuntimeError("Unable to capture a complete PNG after 3 attempts")
    xml_text = adb.ui_xml()
    root = ET.fromstring(xml_text)
    records = node_records(root)
    detected_sensitive = any(
        SENSITIVE.search(r["text"]) or SENSITIVE.search(r["content_desc"])
        for r in records
    )
    actual_scope = "sensitive" if args.scope == "sensitive" or detected_sensitive else "public"
    signature = sha(
        "\n".join(
            f"{r['class']}|{r['text']}|{r['content_desc']}|{r['resource_id']}|{r['clickable']}"
            for r in records
            if r["text"] or r["content_desc"] or r["clickable"]
        )
        + focus
    )

    version_dir = f"v{adb.package_version_name(TARGET_PACKAGE)}_{now:%Y%m%d}"
    raw_shots = RESEARCH / "screenshots" / version_dir / "raw"
    raw_ui = RESEARCH / "ui-hierarchy" / version_dir / "raw"
    processed_ui = RESEARCH / "ui-hierarchy" / version_dir
    meta_dir = RESEARCH / "metadata" / version_dir / "raw"
    shot_path = raw_shots / f"{stamp}_{safe_label}.png"
    xml_path = raw_ui / f"{stamp}_{safe_label}.xml"
    meta_path = meta_dir / f"{stamp}_{safe_label}.json"
    public_summary = processed_ui / f"{stamp}_{safe_label}_summary.md"
    shot_path.parent.mkdir(parents=True, exist_ok=True)
    xml_path.parent.mkdir(parents=True, exist_ok=True)
    public_summary.parent.mkdir(parents=True, exist_ok=True)
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    shot_path.write_bytes(png)
    xml_path.write_text(xml_text, encoding="utf-8")
    if actual_scope == "sensitive":
        public_xml = processed_ui / f"{stamp}_{safe_label}_redacted.xml"
        public_xml.write_text(sanitize_xml(root), encoding="utf-8")
        public_records = node_records(root, redact=True)
    else:
        public_records = records
    public_summary.write_text(summary_markdown(args.label, {
        "captured_at": now.isoformat(),
        "focus": focus,
        "signature": signature,
        "scope": actual_scope,
    }, public_records), encoding="utf-8")

    meta = {
        "label": args.label,
        "captured_at": now.isoformat(),
        "scope": actual_scope,
        "sensitive_detected": detected_sensitive,
        "focus": focus,
        "signature": signature,
        "package": TARGET_PACKAGE,
        "version_dir": version_dir,
        "screenshot": str(shot_path.relative_to(ROOT)),
        "ui_xml": str(xml_path.relative_to(ROOT)),
        "summary": str(public_summary.relative_to(ROOT)),
        "privacy": "raw evidence; inspect and redact before sharing",
    }
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(meta, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
