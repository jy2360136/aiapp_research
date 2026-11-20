from __future__ import annotations

import argparse
import json
import re
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from adb_common import Adb, TARGET_ACTIVITY, TARGET_PACKAGE

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research" / "target-dongzheng-ai"


def n(pattern: str, text: str) -> int | None:
    m = re.search(pattern, text)
    return int(m.group(1)) if m else None


def sample(adb: Adb, label: str) -> dict:
    pid = adb.pid_of(TARGET_PACKAGE)
    item = {"label": label, "captured_at": datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(), "pid": pid, "focus": adb.current_focus()}
    if pid is None:
        item.update({"process_alive": False, "total_pss_kb": 0, "activities": 0, "webviews": 0})
        return item
    text = adb.shell_args(["dumpsys", "meminfo", TARGET_PACKAGE], timeout=45)
    item.update({
        "process_alive": True,
        "total_pss_kb": n(r"TOTAL PSS:\s*(\d+)", text),
        "total_rss_kb": n(r"TOTAL RSS:\s*(\d+)", text),
        "java_heap_kb": n(r"Java Heap:\s*(\d+)", text),
        "native_heap_kb": n(r"Native Heap:\s*(\d+)", text),
        "graphics_kb": n(r"Graphics:\s*(\d+)", text),
        "activities": n(r"Activities:\s*(\d+)", text),
        "webviews": n(r"WebViews:\s*(\d+)", text),
        "views": n(r"Views:\s*(\d+)", text),
    })
    return item


def tap(adb: Adb, x: int, y: int, wait: float = 0.9) -> None:
    adb.tap(x, y)
    time.sleep(wait)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cycles", type=int, default=3)
    args = parser.parse_args()

    adb = Adb()
    adb.require_device()
    adb.shell_args(["am", "force-stop", TARGET_PACKAGE])
    time.sleep(0.7)
    adb.shell_args(["am", "start", "-W", "-n", TARGET_ACTIVITY], timeout=45)
    time.sleep(6)
    rows = [sample(adb, "cold_start_6s")]

    for cycle in range(1, args.cycles + 1):
        # Drawer -> Settings -> Privacy -> Privacy policy WebView
        tap(adb, 95, 212)
        tap(adb, 990, 215)
        tap(adb, 632, 557)
        tap(adb, 632, 380, wait=2.5)
        # Return to main, close drawer, leaving the visited Activity/WebView state behind.
        for _ in range(3):
            adb.keyevent(4)
            time.sleep(0.7)
        tap(adb, 1220, 1400)
        time.sleep(1.2)
        rows.append(sample(adb, f"after_cycle_{cycle}"))

    now = datetime.now(ZoneInfo("Asia/Shanghai"))
    version_dir = f"v{adb.package_version_name(TARGET_PACKAGE)}_{now:%Y%m%d}"
    out = RESEARCH / "logs" / version_dir / "memory"
    raw_out = out / "raw"
    out.mkdir(parents=True, exist_ok=True)
    raw_out.mkdir(parents=True, exist_ok=True)
    stamp = now.strftime("%Y%m%d_%H%M%S")
    json_path = raw_out / f"{stamp}_cycle_test.json"
    json_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# 掌小宝 WebView/页面遍历内存复测",
        "",
        f"- 采集时间：{now.isoformat()}",
        f"- 设备：HONOR MEP-AN00 / Android 16",
        f"- 路径：冷启动 → 侧边栏 → 设置 → 隐私设置 → 隐私政策 WebView → 返回首页，重复 {args.cycles} 次",
        "",
        "| 阶段 | PID | PSS KB | RSS KB | Activities | WebViews | Views |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(f"| {row['label']} | {row['pid'] or '-'} | {row['total_pss_kb']} | {row['total_rss_kb']} | {row['activities']} | {row['webviews']} | {row.get('views', '-')} |")
    lines.extend(["", "说明：PSS 是系统统计的进程总内存近似值；一次结果不能单独证明泄漏，需要结合重复循环趋势、Activity/WebView 数量和系统 Low Memory Kill 记录判断。"])
    md_path = out / f"{stamp}_cycle_test.md"
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"json": str(json_path), "markdown": str(md_path), "rows": rows}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
