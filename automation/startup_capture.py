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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--label", required=True)
    parser.add_argument("--package", default=TARGET_PACKAGE)
    parser.add_argument("--activity", default=TARGET_ACTIVITY)
    parser.add_argument("--intervals", default="0,1,2,3,5,8,12")
    parser.add_argument("--no-force-stop", action="store_true")
    args = parser.parse_args()

    adb = Adb()
    adb.require_device()
    if not args.no_force_stop:
        adb.shell_args(["am", "force-stop", args.package])
        time.sleep(0.8)
    intervals = [float(x) for x in args.intervals.split(",")]
    t0 = time.perf_counter()
    start = adb.shell_args(["am", "start", "-W", "-n", args.activity], timeout=45)
    start_elapsed = time.perf_counter() - t0
    now = datetime.now(ZoneInfo("Asia/Shanghai"))
    stamp = now.strftime("%Y%m%d_%H%M%S")
    version_dir = f"v{adb.package_version_name(args.package)}_{now:%Y%m%d}"
    shot_dir = RESEARCH / "screenshots" / version_dir / "startup" / "raw" / f"{stamp}_{args.label}"
    meta_dir = RESEARCH / "metadata" / version_dir / "startup" / "raw"
    shot_dir.mkdir(parents=True, exist_ok=True)
    meta_dir.mkdir(parents=True, exist_ok=True)
    records = []
    for order, elapsed in enumerate(intervals):
        delay = elapsed - (time.perf_counter() - t0)
        if delay > 0:
            time.sleep(delay)
        png = adb.screenshot_png()
        with Image.open(io.BytesIO(png)) as image:
            image.verify()
        actual = time.perf_counter() - t0
        path = shot_dir / f"{order:02d}_{actual:.2f}s.png"
        path.write_bytes(png)
        records.append({"target_seconds": elapsed, "actual_seconds": round(actual, 3), "path": str(path.relative_to(ROOT))})
    meta_path = meta_dir / f"{stamp}_{args.label}_metadata.json"
    meta_path.write_text(json.dumps({
        "label": args.label,
        "started_at": now.isoformat(),
        "activity": args.activity,
        "start_output": start,
        "start_return_seconds": round(start_elapsed, 3),
        "focus": adb.current_focus(),
        "screenshots": records,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"label": args.label, "start_return_seconds": round(start_elapsed, 3), "screenshots": str(shot_dir), "metadata": str(meta_path), "records": records}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
