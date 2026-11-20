from __future__ import annotations

import argparse
import io
import json
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from PIL import Image

from adb_common import Adb, TARGET_ACTIVITY, TARGET_PACKAGE

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research" / "target-dongzheng-ai"


def tap(adb: Adb, x: int, y: int, wait: float = 0.7) -> None:
    adb.tap(x, y)
    time.sleep(wait)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--query", default="600519")
    parser.add_argument("--response-wait", type=float, default=25)
    args = parser.parse_args()

    adb = Adb()
    adb.require_device()
    now = datetime.now(ZoneInfo("Asia/Shanghai"))
    version_dir = f"v{adb.package_version_name(TARGET_PACKAGE)}_{now:%Y%m%d}"
    trial_name = now.strftime("%Y%m%d_%H%M%S")
    shot_dir = RESEARCH / "screenshots" / version_dir / "ai-trials" / "raw"
    ui_dir = RESEARCH / "ui-hierarchy" / version_dir / "ai-trials" / "raw"
    meta_dir = RESEARCH / "metadata" / version_dir / "ai-trials" / "raw"
    for folder in (shot_dir, ui_dir, meta_dir): folder.mkdir(parents=True, exist_ok=True)
    rows = []
    for trial in range(1, args.trials + 1):
        adb.shell_args(["am", "force-stop", TARGET_PACKAGE])
        time.sleep(0.8)
        start = adb.shell_args(["am", "start", "-W", "-n", TARGET_ACTIVITY], timeout=45)
        time.sleep(6)
        tap(adb, 632, 212)             # 对话
        tap(adb, 920, 2451)            # voice -> text input
        tap(adb, 520, 2451)            # focus input
        for ch in args.query:
            adb.shell_args(["input", "text", ch])
            time.sleep(0.18)
        time.sleep(0.8)
        adb.keyevent(66)               # IME search/send
        time.sleep(args.response_wait)
        png = adb.screenshot_png()
        with Image.open(io.BytesIO(png)) as image:
            image.verify()
        shot = shot_dir / f"{trial_name}_trial_{trial:02d}.png"
        shot.write_bytes(png)
        xml_text = adb.ui_xml()
        ui = ui_dir / f"{trial_name}_trial_{trial:02d}.xml"
        ui.write_text(xml_text, encoding="utf-8")
        rows.append({
            "trial": trial,
            "start": start,
            "focus": adb.current_focus(),
            "screenshot": str(shot.relative_to(ROOT)),
            "ui_xml": str(ui.relative_to(ROOT)),
            "service_error_in_tree": "服务开小差了" in xml_text,
            "stock_answer_in_tree": "贵州茅台" in xml_text,
            "response_text_in_tree": "行情" in xml_text or "开盘价" in xml_text or "K线" in xml_text,
            "captured_at": datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(),
        })
    meta_path = meta_dir / f"{trial_name}_metadata.json"
    meta_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"screenshots": str(shot_dir), "ui_xml": str(ui_dir), "metadata": str(meta_path), "rows": rows}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
