from __future__ import annotations

import json
import re
import sys

from adb_common import Adb, TARGET_PACKAGE


def package_meta(adb: Adb, package: str) -> dict:
    raw = adb.shell_args(["dumpsys", "package", package])
    fields = {}
    patterns = {
        "version_name": r"versionName=([^\s]+)",
        "version_code": r"versionCode=(\d+)",
        "first_install_time": r"firstInstallTime=([^\n]+)",
        "last_update_time": r"lastUpdateTime=([^\n]+)",
        "target_sdk": r"targetSdk=(\d+)",
        "min_sdk": r"minSdk=(\d+)",
    }
    for key, pattern in patterns.items():
        match = re.search(pattern, raw)
        fields[key] = match.group(1).strip() if match else None
    fields["debuggable"] = "DEBUGGABLE" in raw
    return fields


def main() -> int:
    adb = Adb()
    adb.require_device()
    devices = adb.devices()
    result = {
        "adb": adb.adb,
        "serial": adb.serial,
        "devices": devices,
        "manufacturer": adb.shell("getprop ro.product.manufacturer").strip(),
        "model": adb.shell("getprop ro.product.model").strip(),
        "android": adb.shell("getprop ro.build.version.release").strip(),
        "sdk": adb.shell("getprop ro.build.version.sdk").strip(),
        "screen": adb.shell("wm size").strip(),
        "density": adb.shell("wm density").strip(),
        "focus": adb.current_focus(),
        "target_pid": adb.pid_of(TARGET_PACKAGE),
        "target_package": TARGET_PACKAGE,
        "target_meta": package_meta(adb, TARGET_PACKAGE),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
