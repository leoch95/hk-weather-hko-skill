# ROADMAP — hk-weather-hko

> 資料來源與官方文檔：
> - HKO Open Data API Documentation (PDF, v1.13, Sep 2025)
> - https://www.hko.gov.hk/tc/abouthko/opendata_intro.htm
> - https://data.gov.hk/tc-datasets/provider/hk-hko

---

## P0 — 合規 / 授權 ✅ Done

| 項目 | 狀態 | 說明 |
|------|------|------|
| 移除「可商用」錯誤描述 | ✅ | SKILL.md / api-docs.md 已修正 |
| 「Code vs Data」授權分離 | ✅ | terms-and-attribution.md / README.md 已加 |
| README 加「不關聯」聲明 | ✅ | README.md 已加 |
| 官方條款連結 | ✅ | 三份 reference + README 已附連結 |

---

## P1 — 天氣功能增強

### P1.1 — `warningInfo` 詳細警告內容
- **現況**：只用 `warnsum`（摘要），唔顯示警告全文
- **目標**：新增 `--type warning-detail` 或自動偵測到有警告時 fallback 拉 `warningInfo`，回覆帶「官方文字摘要」
- **API**：`dataType=warningInfo`（weather.php）
- **來源**：官方 PDF p.6, p.17；api-docs.md L17-L19

### P1.2 — `swt` 特別天氣提示
- **現況**：未支援
- **目標**：新增 `--type tips` 或 heartbeat check 自動偵測；適合「今晚/明早要注意乜」場景
- **API**：`dataType=swt`（weather.php）
- **來源**：官方 PDF p.6；api-docs.md L18

### P1.3 — 九天預報輸出補齊 PSR / ForecastIcon
- **現況**：`format_forecast()` 唔輸出 PSR（顯著降雨機會）同 ForecastIcon
- **目標**：加入 PSR 顯示（低/中低/中/中高/高）+ icon code → emoji 映射
- **API**：`fnd` response 已有 `PSR` 同 `ForecastIcon` 欄位
- **來源**：官方 PDF p.7；fetch_weather.py L140-L178

### P1.4 — UV Index / Lightning 結構化解析
- **現況**：`format_current_weather()` 對 uvindex 只做 truthy check，冇解析 object 結構；lightning 完全未處理
- **目標**：正確解析 `uvindex.data[].value` / `uvindex.data[].desc`；新增 `lightning.occur` + `lightning.startTime` 顯示
- **API**：`rhrread` response
- **來源**：官方 PDF p.8-9；fetch_weather.py L129-L136

### P1.5 — Licensing 章節（README 首頁）
- **現況**：README 已加授權摘要 ✅
- **目標**：如有需要，進一步加入官方要求之免責聲明框架文字（link + 指引）

---

## P2 — 高頻降雨 / 擴展端點

### P2.1 — hourlyRainfall.php（自動氣象站過去一小時雨量）
- **現況**：未支援（而家用 `rhrread` rainfall data，更新頻率較低）
- **目標**：新增 `--type station-rainfall`；回答「而家邊度落緊雨？」
- **API**：`https://data.weather.gov.hk/weatherAPI/opendata/hourlyRainfall.php`（每15分鐘更新，臨時數據）
- **來源**：官方 PDF p.41；opendata_intro.htm
- **注意**：輸出須標註「臨時數據，只經有限度驗證」

### P2.2 — 網格點降雨臨近預報（Gridded Rainfall Nowcast）
- **現況**：未支援
- **目標**：支援「未來兩小時會唔會落雨」嘅 nowcast
- **API**：data.gov.hk dataset（每12分鐘更新）
- **來源**：opendata_intro.htm

### P2.3 — opendata.php 日出日落 / 潮汐 / 能見度 / 閃電次數
- **現況**：未支援
- **目標**：按需加入 `SRS`（日出日落）、`HHOT`/`HLT`（潮汐）、`LTMV`（能見度）、`LHL`（閃電次數）
- **API**：`https://data.weather.gov.hk/weatherAPI/opendata/opendata.php`
- **來源**：官方 PDF p.24-35

### P2.4 — 歷史天氣數據
- **現況**：未支援
- **目標**：回答「噚日最高幾度？」等問題（`CLMTEMP` / `CLMMAXT` / `CLMMINT` / `RYES`）
- **API**：opendata.php
- **來源**：官方 PDF p.28-36

---

## P3 — HKO 綜合（可選 — 會改變 skill 定位）

### P3.1 — earthquake.php 地震速報 / 有感地震
- **API**：`https://data.weather.gov.hk/weatherAPI/opendata/earthquake.php`（`qem` / `feltearthquake`）
- **來源**：官方 PDF p.22

### P3.2 — lunardate.php 農曆轉換
- **API**：`https://data.weather.gov.hk/weatherAPI/opendata/lunardate.php`
- **來源**：官方 PDF p.40

---

## 工程質量

| 項目 | 優先度 | 說明 |
|------|--------|------|
| Cache / updateTime | P1 | 利用 API response `updateTime` 避免重複拉取 |
| Retry + backoff | P1 | 網絡錯誤 / 503 自動重試 |
| Golden tests（JSON fixtures） | P1 | 用 `--json` 存樣本，regression testing |
| 臨時數據標籤 | P2 | 高頻數據輸出自動加「臨時數據」提示 |
| CI lint / test | P1 | GitHub Actions |
| ClawHub 自動發佈 | P2 | tag → release → clawhub publish |

---

*Last updated: 2026-03-22*
