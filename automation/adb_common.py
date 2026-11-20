from __future__ import annotations

import os
import re
import shutil
import subprocess
import time
from pathlib import Path

TARGET_PACKAGE = "dongzheng.ai.android.phone"
TARGET_ACTIVITY = f"{TARGET_PACKAGE}/.MainActivity"


def _candidate_adb_paths() -> list[Path]:
    candidates: list[Path] = []
    env_adb = os.environ.get("ADB")
    if env_adb:
        candidates.append(Path(env_adb))
    which = shutil.which("adb")
    if which:
        candidates.append(Path(which))
    local = Path(os.environ.get("LOCALAPPDATA", ""))
    candidates.extend(local.glob("Microsoft/WinGet/Packages/Google.PlatformTools_*/platform-tools/adb.exe"))
    candidates.extend([
        local / "Android/Sdk/platform-tools/adb.exe",
        Path(r"C:\Android\platform-tools\adb.exe"),
    ])
    return candidates


def find_adb() -> str:
    for candidate in _candidate_adb_paths():
        if candidate.is_file():
            return str(candidate)
    raise FileNotFoundError("adb not found. Install Android SDK Platform-Tools or set ADB.")


class Adb:
    def __init__(self, serial: str | None = None) -> None:
        self.adb = find_adb()
        self.serial = serial

    def _prefix(self) -> list[str]:
        cmd = [self.adb]
        if self.serial:
            cmd.extend(["-s", self.serial])
        return cmd

    def run(self, args: list[str], *, timeout: int = 30, check: bool = True) -> subprocess.CompletedProcess[bytes]:
        last: subprocess.CompletedProcess[bytes] | None = None
        for attempt in range(3):
            last = subprocess.run(self._prefix() + args, capture_output=True, timeout=timeout)
            err = last.stderr.decode("utf-8", errors="replace")
            transient = "device" in err and ("not found" in err or "no devices" in err)
            if last.returncode == 0 or not transient or attempt == 2:
                break
            subprocess.run([self.adb, "kill-server"], capture_output=True, timeout=15)
            time.sleep(0.7)
            subprocess.run([self.adb, "start-server"], capture_output=True, timeout=15)
            time.sleep(1.5)
        assert last is not None
        if check and last.returncode != 0:
            err = last.stderr.decode("utf-8", errors="replace")
            raise RuntimeError(f"adb command failed ({last.returncode}): {' '.join(args)}\n{err}")
        return last

    def text(self, args: list[str], *, timeout: int = 30) -> str:
        return self.run(args, timeout=timeout).stdout.decode("utf-8", errors="replace")

    def devices(self) -> list[dict[str, str]]:
        out = self.text(["devices", "-l"])
        devices = []
        for line in out.splitlines():
            line = line.strip()
            if not line or line.startswith("List of devices"):
                continue
            parts = line.split()
            if len(parts) >= 2:
                devices.append({"serial": parts[0], "state": parts[1], "detail": " ".join(parts[2:])})
        return devices

    def require_device(self) -> None:
        devices = self.devices()
        ready = [d for d in devices if d["state"] == "device"]
        if not ready:
            subprocess.run([self.adb, "kill-server"], capture_output=True, timeout=15)
            time.sleep(0.7)
            subprocess.run([self.adb, "start-server"], capture_output=True, timeout=15)
            time.sleep(2)
            devices = self.devices()
            ready = [d for d in devices if d["state"] == "device"]
        if not ready:
            raise RuntimeError(f"No authorized adb device. Current devices: {devices}")
        if not self.serial:
            self.serial = ready[0]["serial"]

    def shell(self, command: str, *, timeout: int = 30) -> str:
        return self.text(["shell", command], timeout=timeout)

    def shell_args(self, args: list[str], *, timeout: int = 30, check: bool = True) -> str:
        return self.run(["shell", *args], timeout=timeout, check=check).stdout.decode("utf-8", errors="replace")

    def current_focus(self) -> str:
        out = self.shell("dumpsys window")
        lines = [line.strip() for line in out.splitlines() if "mCurrentFocus=" in line or "mFocusedApp=" in line]
        return "\n".join(lines)

    def foreground_is_package(self, package: str) -> bool:
        return package in self.current_focus()

    def foreground_is_target(self) -> bool:
        return self.foreground_is_package(TARGET_PACKAGE)

    def bring_package_to_front(self, package: str, activity: str) -> None:
        if not self.foreground_is_package(package):
            self.shell_args(["am", "start", "-W", "-n", activity])
        if not self.foreground_is_package(package):
            raise RuntimeError(f"Package {package} is not foreground after am start")

    def bring_target_to_front(self) -> None:
        self.bring_package_to_front(TARGET_PACKAGE, TARGET_ACTIVITY)

    def pid_of(self, package: str = TARGET_PACKAGE) -> int | None:
        result = self.run(["shell", "pidof", package], check=False)
        value = result.stdout.decode("utf-8", errors="replace").strip()
        if not value:
            return None
        return int(value.split()[0])

    def package_version_name(self, package: str) -> str:
        raw = self.shell_args(["dumpsys", "package", package])
        match = re.search(r"versionName=([^\s]+)", raw)
        return match.group(1).strip() if match else "unknown"

    def tap(self, x: int, y: int) -> None:
        self.shell_args(["input", "tap", str(x), str(y)])

    def keyevent(self, code: int) -> None:
        self.shell_args(["input", "keyevent", str(code)])

    def screenshot_png(self) -> bytes:
        return self.run(["exec-out", "screencap", "-p"], timeout=30).stdout

    def ui_xml(self) -> str:
        remote = "/sdcard/window_dump.xml"
        self.shell_args(["uiautomator", "dump", remote], timeout=30)
        data = self.run(["exec-out", "cat", remote], timeout=30).stdout
        self.shell_args(["rm", remote], timeout=10, check=False)
        return data.decode("utf-8", errors="replace")

    def dump_logcat(self, pid: int | None = None, *, clear: bool = False) -> str:
        if clear:
            self.run(["logcat", "-c"], timeout=15)
        args = ["logcat", "-d", "-v", "threadtime"]
        if pid is not None:
            args.append(f"--pid={pid}")
        return self.text(args, timeout=45)
