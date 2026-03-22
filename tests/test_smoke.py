import json
import subprocess
import sys


def run(cmd):
    return subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )


def test_fetch_current_json_has_temperature():
    p = run([sys.executable, "scripts/fetch_weather.py", "--type", "current", "--json"])
    assert p.returncode == 0, p.stderr
    data = json.loads(p.stdout)
    assert "temperature" in data


def test_fetch_hourly_text_does_not_crash():
    p = run([sys.executable, "scripts/fetch_weather.py", "--type", "hourly"])
    assert p.returncode == 0, p.stderr
    assert p.stdout.strip() != ""
