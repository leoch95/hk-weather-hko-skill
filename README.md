# hk-weather-hko-skill

OpenClaw skill：使用香港天文台（HKO）開放數據 API 查詢香港天氣。

## 功能

- 全港即時天氣（`rhrread`）
- 分區 / 監測站氣溫、降雨（`rhrread`）
- 本地天氣預報概況（`flw`）
- 九天預報（`fnd`）
- 天氣警告摘要（`warnsum`）
- 過去一小時分區降雨資訊（`rhrread`）
- 未來幾日降雨預報整理（`fnd`）

> 資料來源：香港天文台（HKO）

## 使用（本地測試腳本）

```bash
# 全港即時天氣
python3 scripts/fetch_weather.py --type current

# 指定地區（監測站）
python3 scripts/fetch_weather.py --type regional --location 沙田

# 顯示全部監測站氣溫
python3 scripts/fetch_weather.py --type regional

# 九天預報
python3 scripts/fetch_weather.py --type forecast --days 9

# 三天天氣預報
python3 scripts/fetch_weather.py --type forecast --days 3

# 本地天氣預報（概況）
python3 scripts/fetch_weather.py --type hourly

# 過去一小時分區降雨
python3 scripts/fetch_weather.py --type rainfall

# 未來幾日降雨預報
python3 scripts/fetch_weather.py --type rainfall-forecast --days 9

# 天氣警告（經 fetch_weather.py）
python3 scripts/fetch_weather.py --type warnings

# 天氣警告
python3 scripts/check_warnings.py

# 僅檢查關鍵警告
python3 scripts/check_warnings.py --critical

# 輸出原始 JSON
python3 scripts/fetch_weather.py --type current --json
```

## Skill 用法

見 `SKILL.md`（Skill name：`hk-weather-hko`）。

## Tests

```bash
python3 -m compileall scripts tests
python3 tests/run_tests.py
```

## ⚠️ 授權與使用條款

- **Code（本 repo 代碼）**：MIT License（見 `LICENSE`）
- **Data（天文台 API 輸出之資料）**：**不受 MIT 覆蓋**。使用、再分發、或商業應用 HKO 資料須遵守香港天文台／香港特別行政區政府的使用條件。商業用途可能需要天文台書面授權。
  - [知識產權公告](https://www.hko.gov.hk/tc/readme/readme.htm)
  - [非商業用途條件](https://www.hko.gov.hk/tc/appweb/applink.htm)
  - [商業用途條件](https://www.hko.gov.hk/tc/appweb/commercial.htm)
- 最低要求：展示「**資料來源：香港天文台**」及按官方條款展示免責聲明。
- 本專案與香港天文台**無任何合作或關聯**。

詳見 `references/terms-and-attribution.md`。
