#!/usr/bin/env python3
"""Minimal offline tests (no third-party deps).

This repo is intended to be easy to run in CI without pip.
We validate that:
- formatters do not crash on representative fixtures
- CLI entrypoints run

Note: Fixtures are captured from HKO Open Data responses.
"""

from __future__ import annotations

import json
import subprocess
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "tests" / "fixtures"


def load_module(path: Path):
    spec = spec_from_file_location(path.stem, path)
    assert spec and spec.loader
    mod = module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[attr-defined]
    return mod


def test_formatters(fetch_weather):
    rhr = json.loads((FIX / "rhrread.json").read_text(encoding="utf-8"))
    flw = json.loads((FIX / "flw.json").read_text(encoding="utf-8"))
    fnd = json.loads((FIX / "fnd.json").read_text(encoding="utf-8"))
    warn = json.loads((FIX / "warnsum.json").read_text(encoding="utf-8"))

    out1 = fetch_weather.format_current_weather(rhr)
    assert isinstance(out1, str) and out1.strip()

    out2 = fetch_weather.format_hourly(flw)
    assert isinstance(out2, str) and out2.strip()

    out3 = fetch_weather.format_forecast(fnd, days=3)
    assert isinstance(out3, str) and out3.strip()

    out4 = fetch_weather.format_warnings(warn)
    assert isinstance(out4, str) and out4.strip()


def test_cli_smoke():
    # Should run without crashing. Uses live HKO API.
    # Keep it lightweight.
    cmd = [sys.executable, str(ROOT / "scripts" / "fetch_weather.py"), "--type", "current"]
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    assert p.returncode == 0, p.stderr


def main() -> int:
    fetch_weather = load_module(ROOT / "scripts" / "fetch_weather.py")

    test_formatters(fetch_weather)
    test_cli_smoke()

    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
