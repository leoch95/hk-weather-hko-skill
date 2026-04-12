# Copilot instructions for `hk-weather-hko-skill`

## Build, test, and lint

```bash
# Syntax/build-equivalent check used by CI
python3 -m compileall scripts tests

# Main test command used by CI (no third-party dependencies)
python3 tests/run_tests.py

# Pytest smoke tests, if pytest is installed locally
python3 -m pytest tests/test_smoke.py -q

# Run a single smoke test, if pytest is installed locally
python3 -m pytest tests/test_smoke.py::test_fetch_current_json_has_temperature -q

# Lint, if ruff is installed locally
python3 -m ruff check .
```

`tests/run_tests.py` is the canonical low-dependency test path. There is no package build step; CI uses `compileall` as the syntax gate before running tests.

## High-level architecture

This repository is an OpenClaw/ClawHub skill, not a packaged Python library. The runtime surface that gets shipped is defined by `SKILL.md` and the files copied in `.github/workflows/release.yml`: `scripts/`, `references/`, and `SKILL.md`.

- `scripts/fetch_weather.py` is the main CLI entrypoint. It maps user-facing `--type` values to HKO `dataType` values, fetches JSON from the HKO Open Data API with the Python standard library, and formats human-readable output for current weather, regional weather, forecasts, rainfall, and warnings.
- `scripts/check_warnings.py` is a smaller warning-focused CLI around `warnsum`, including a `--critical` filter for high-risk alerts.
- `tests/run_tests.py` is the CI-friendly harness. It imports `scripts/fetch_weather.py` directly by file path and exercises formatter functions against checked-in JSON fixtures in `tests/fixtures/`, plus one live CLI smoke call.
- `tests/test_smoke.py` provides pytest-style smoke coverage for the CLI, but pytest is not required for the main CI path.
- `references/` contains the HKO API notes, script usage docs, warning reference, and attribution/licensing requirements that the skill and scripts are expected to follow.

## Key conventions

- Keep the runtime dependency-free. The repo is designed to run in CI without `pip install`; prefer Python standard-library solutions unless the task explicitly changes that constraint.
- Prefer extending the existing CLI scripts instead of bypassing them with direct API calls. `SKILL.md` and `README.md` both treat the scripts as the supported interface for weather lookups.
- Preserve Traditional Chinese as the default user-facing language and output style. The scripts default to `lang=tc`, and the help text, docs, and formatted responses are written for Traditional Chinese users.
- Use the real HKO `dataType` values from `references/api-docs.md`: `rhrread`, `flw`, `fnd`, `warnsum`, `warningInfo`, and `swt`. Regional temperature and rainfall both come from `rhrread`; do not introduce older placeholder names like `RegionalWeather` or `WarningSummary`.
- When changing warning naming or filtering, keep `scripts/fetch_weather.py`, `scripts/check_warnings.py`, and `references/warnings.md` aligned. Warning name fallbacks should continue to handle unknown codes gracefully.
- When adding or moving runtime files, check `.github/workflows/release.yml`. The release job only publishes `scripts/`, `references/`, and `SKILL.md`, so helpers placed elsewhere will not ship unless the workflow is updated too.
- Keep the HKO attribution and disclaimer requirements intact in docs and generated outputs: include `資料來源：香港天文台`, avoid implying official affiliation, and do not position this project for safety-critical use.
