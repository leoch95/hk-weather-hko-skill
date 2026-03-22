# hk-weather-hko-skill

OpenClaw skill：使用香港天文台（HKO）開放數據 API 查詢香港天氣。

## 功能

- 全港即時天氣（`rhrread`）
- 分區 / 監測站氣溫、降雨（`rhrread`）
- 本地天氣預報概況（`flw`）
- 九天預報（`fnd`）
- 天氣警告摘要（`warnsum`）

> 資料來源：香港天文台（HKO）

## 使用（本地測試腳本）

```bash
# 全港即時天氣
python3 scripts/fetch_weather.py --type current

# 指定地區（監測站）
python3 scripts/fetch_weather.py --type regional --location 沙田

# 九天預報
python3 scripts/fetch_weather.py --type forecast --days 9

# 本地天氣預報（概況）
python3 scripts/fetch_weather.py --type hourly

# 天氣警告
python3 scripts/check_warnings.py
```

## Skill 用法

見 `SKILL.md`（Skill name：`hk-weather-hko`）。

## Tests

```bash
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
