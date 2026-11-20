from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from adb_common import Adb, TARGET_PACKAGE

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research" / "target-dongzheng-ai"
KEY = re.compile(r"(FATAL EXCEPTION|AndroidRuntime|ANR in|ANR |Exception|Error|Crash|SIG(?:SEGV|ABRT|BUS)|NullPointer|IllegalState|NetworkOnMainThread)")


def sanitize(line: str) -> str:
    line = re.sub(r"(?i)(bearer\s+)[A-Za-z0-9._\-+/=]+", r"\1[REDACTED]", line)
    line = re.sub(r"(?i)(token|cookie|password|passwd|authorization)=([^&\s]+)", r"\1=[REDACTED]", line)
    line = re.sub(r"(?<!\d)1[3-9]\d{9}(?!\d)", "[PHONE]", line)
    line = re.sub(r"(?<!\w)(?:\d[ *]{0,4}){8,}\d(?!\w)", "[LONG_ID]", line)
    return line


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--label", required=True)
    parser.add_argument("--clear", action="store_true", help="Clear logcat before collecting")
    parser.add_argument("--seconds", type=float, default=0, help="Wait after optional clear")
    args = parser.parse_args()

    adb = Adb()
    adb.require_device()
    pid = adb.pid_of(TARGET_PACKAGE)
    if args.clear:
        adb.dump_logcat(pid=pid, clear=True)
        if args.seconds:
            import time
            time.sleep(args.seconds)
    raw = adb.dump_logcat(pid=pid)
    now = datetime.now(ZoneInfo("Asia/Shanghai"))
    stamp = now.strftime("%Y%m%d_%H%M%S")
    safe_label = re.sub(r"[^0-9A-Za-z_\-\u4e00-\u9fff]+", "_", args.label).strip("_")
    version_dir = f"v{adb.package_version_name(TARGET_PACKAGE)}_{now:%Y%m%d}"
    raw_dir = RESEARCH / "logs" / version_dir / "raw"
    report_dir = RESEARCH / "logs" / version_dir
    raw_dir.mkdir(parents=True, exist_ok=True)
    report_dir.mkdir(parents=True, exist_ok=True)
    raw_path = raw_dir / f"{stamp}_{safe_label}.log"
    raw_path.write_text(raw, encoding="utf-8")

    selected = []
    seen = set()
    for line in raw.splitlines():
        if KEY.search(line):
            clean = sanitize(line).strip()
            if clean not in seen:
                selected.append(clean)
                seen.add(clean)
    report = report_dir / f"{stamp}_{safe_label}_exceptions.md"
    content = [
        f"# 异常日志摘要：{args.label}",
        "",
        f"- 采集时间：{now.isoformat()}",
        f"- 进程 PID：{pid}",
        f"- 原始日志：`{raw_path.relative_to(ROOT).as_posix()}`（敏感，勿外发）",
        f"- 命中行数：{len(selected)}",
        "",
        "```text",
        *(selected if selected else ["未命中 FATAL / Exception / ANR / Crash 等关键词。"]),
        "```",
        "",
        "说明：完整原始 logcat 可能包含敏感信息，不得对外分享；本文件仅保留经基础脱敏的关键行，仍需人工复核。",
    ]
    report.write_text("\n".join(content) + "\n", encoding="utf-8")
    print(f"raw={raw_path}")
    print(f"report={report}")
    print(f"matches={len(selected)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
