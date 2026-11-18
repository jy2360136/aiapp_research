from __future__ import annotations

import argparse
import io
import json
import re
import time
from datetime import datetime
from pathlib import Path
from xml.etree import ElementTree as ET
from zoneinfo import ZoneInfo

from PIL import Image

from adb_common import Adb

ROOT = Path(__file__).resolve().parents[1]
PRIVATE = ROOT / ".private" / "raw" / "competitors"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", required=True)
    parser.add_argument("--activity", required=True)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--label", required=True)
    parser.add_argument("--wait-ms", type=int, default=5000)
    parser.add_argument("--no-force-stop", action="store_true")
    parser.add_argument("--no-start", action="store_true", help="Capture current screen without launching the app")
    args = parser.parse_args()

    adb = Adb()
    adb.require_device()
    start = ""
    if not args.no_start:
        if not args.no_force_stop:
            adb.shell_args(["am", "force-stop", args.package])
            time.sleep(0.8)
        start = adb.shell_args(["am", "start", "-W", "-n", args.activity], timeout=45)
        time.sleep(args.wait_ms / 1000)

    png = b""
    for _ in range(3):
        candidate = adb.screenshot_png()
        try:
            with Image.open(io.BytesIO(candidate)) as image:
                image.verify()
            png = candidate
            break
        except Exception:
            time.sleep(0.8)
    if not png:
        raise RuntimeError("Unable to capture complete PNG")

    xml_text = adb.ui_xml()
    ET.fromstring(xml_text)
    focus = adb.current_focus()
    now = datetime.now(ZoneInfo("Asia/Shanghai"))
    stamp = now.strftime("%Y%m%d_%H%M%S")
    safe_label = re.sub(r"[^0-9A-Za-z_\-\u4e00-\u9fff]+", "_", args.label).strip("_")
    out = PRIVATE / args.slug
    shot_dir = out / "screenshots"
    xml_dir = out / "ui-hierarchy"
    meta_dir = out / "metadata"
    for d in (shot_dir, xml_dir, meta_dir):
        d.mkdir(parents=True, exist_ok=True)
    shot = shot_dir / f"{stamp}_{safe_label}.png"
    ui = xml_dir / f"{stamp}_{safe_label}.xml"
    meta = meta_dir / f"{stamp}_{safe_label}.json"
    shot.write_bytes(png)
    ui.write_text(xml_text, encoding="utf-8")
    meta.write_text(json.dumps({
        "package": args.package,
        "activity_requested": args.activity,
        "label": args.label,
        "captured_at": now.isoformat(),
        "focus": focus,
        "pid": adb.pid_of(args.package),
        "start_output": start,
        "screenshot": str(shot.relative_to(ROOT)),
        "ui_xml": str(ui.relative_to(ROOT)),
        "privacy": "raw private evidence; inspect and redact before publishing",
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"package": args.package, "label": args.label, "screenshot": str(shot), "ui_xml": str(ui), "focus": focus}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
