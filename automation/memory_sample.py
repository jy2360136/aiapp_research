from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from adb_common import Adb, TARGET_PACKAGE

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research" / "target-dongzheng-ai"


def first_int(pattern: str, text: str) -> int | None:
    match = re.search(pattern, text)
    return int(match.group(1)) if match else None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--label", required=True)
    parser.add_argument("--package", default=TARGET_PACKAGE)
    args = parser.parse_args()

    adb = Adb()
    adb.require_device()
    pid = adb.pid_of(args.package)
    focus = adb.current_focus()
    now = datetime.now(ZoneInfo("Asia/Shanghai"))
    version_dir = f"v{adb.package_version_name(args.package)}_{now:%Y%m%d}"
    out = RESEARCH / "logs" / version_dir / "memory" / "raw"
    sample: dict = {
        "label": args.label,
        "captured_at": datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(),
        "package": args.package,
        "pid": pid,
        "focus": focus,
    }
    if pid is None:
        sample.update({
            "process_alive": False,
            "total_pss_kb": 0,
            "total_rss_kb": 0,
            "note": "process not running",
        })
    else:
        text = adb.shell_args(["dumpsys", "meminfo", args.package], timeout=45)
        sample.update({
            "process_alive": True,
            "total_pss_kb": first_int(r"TOTAL PSS:\s*(\d+)", text),
            "total_rss_kb": first_int(r"TOTAL RSS:\s*(\d+)", text),
            "java_heap_kb": first_int(r"Java Heap:\s*(\d+)", text),
            "native_heap_kb": first_int(r"Native Heap:\s*(\d+)", text),
            "graphics_kb": first_int(r"Graphics:\s*(\d+)", text),
            "views": first_int(r"Views:\s*(\d+)", text),
            "view_root_impl": first_int(r"ViewRootImpl:\s*(\d+)", text),
            "app_contexts": first_int(r"AppContexts:\s*(\d+)", text),
            "activities": first_int(r"Activities:\s*(\d+)", text),
            "webviews": first_int(r"WebViews:\s*(\d+)", text),
        })
    out.mkdir(parents=True, exist_ok=True)
    stamp = now.strftime("%Y%m%d_%H%M%S")
    path = out / f"{stamp}_{args.label}.json"
    path.write_text(json.dumps(sample, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(sample, ensure_ascii=False, indent=2))
    print(f"saved={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
