## 目的

- [ ] 讓 hk-weather-hko skill repo 達到「可開源、可維護、可發佈」的最低可用狀態（v0.1.0 bootstrap）

## 變更摘要

- 修正：`scripts/fetch_weather.py --type hourly` 之前會因 `format_hourly()` 缺失而 crash；現已補回實作
- 文件：補齊 `references/regions.md`、`references/warnings.md`、`references/terms-and-attribution.md`
- 文件：新增 `README.md`、`CHANGELOG.md`、`.gitignore`
- 指令：`SKILL.md` 所有示例已改用 `{baseDir}`（避免 cwd 不同導致路徑失效）
- CI：新增 GitHub Actions（compileall + `tests/run_tests.py`，不依賴 pip）
- 測試：新增 fixtures + offline tests

## 如何驗證

本地：

```bash
python3 scripts/fetch_weather.py --type current
python3 scripts/fetch_weather.py --type hourly
python3 scripts/check_warnings.py
python3 tests/run_tests.py
```

CI：確認 GitHub Actions `CI` workflow 為綠燈。

## 注意 / 後續

- 目前 skill name 已使用：`hk-weather-hko`（避免與其他 `hk-weather` 撞名）
- 下一步建議：設定 main branch protection（require CI）、再做 v0.1.0 tag/release +（可選）release automation
