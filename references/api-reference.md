# AKShare Open API 参考手册

> 基于 AKShare 1.18.x | 数据来源：东方财富、同花顺、新浪、巨潮资讯等
> 本手册列出本 Skill 封装的所有接口，按类别组织。

## 接口统计

| 类别 | 接口数 |
|------|--------|
| 实时行情 | 14 |
| 历史K线 | 7 |
| 财务数据 | 13 |
| 板块分析 | 6 |
| 资金流向 | 9 |
| 特殊数据 | 60+ |
| 指数数据 | 6 |
| 宏观数据 | 30+ |
| 市场总貌 | 5 |
| **合计** | **150+** |

---

## 1. 实时行情 (stock/spot.py)

| 命令 | 说明 | AKShare 函数 | 耗时 |
|------|------|-------------|------|
| `a-all` | 沪深京全部A股 | `stock_zh_a_spot_em()` | ~70s |
| `sh` | 沪A股 | `stock_sh_a_spot_em()` | ~28s |
| `sz` | 深A股 | `stock_sz_a_spot_em()` | ~28s |
| `bj` | 北证A股 | `stock_bj_a_spot_em()` | ~10s |
| `kc` | 科创板 | `stock_kc_a_spot_em()` | ~10s |
| `cy` | 创业板 | `stock_cy_a_spot_em()` | ~10s |
| `new` | 新股 | `stock_new_a_spot_em()` | ~5s |
| `hk` | 港股实时 | `stock_hk_spot_em()` | ~30s |
| `us` | 美股实时 | `stock_us_spot_em()` | ~30s |
| `ah` | A+H股对比 | `stock_zh_ah_spot_em()` | ~10s |
| `index` | 指数实时 | `stock_zh_index_spot_em()` | ~10s |
| `info` | 个股信息 | `stock_individual_info_em()` | ~3s |
| `bid-ask` | 五档盘口 | `stock_bid_ask_em()` | ~3s |
| `info-xq` | 雪球公司概况 | `stock_individual_basic_info_xq()` | ~5s |

## 2. 历史K线 (stock/hist.py)

| 命令 | 说明 | AKShare 函数 |
|------|------|-------------|
| `a` | A股日/周/月K | `stock_zh_a_hist()` |
| `a-min` | A股分钟K | `stock_zh_a_hist_min_em()` |
| `hk` | 港股K线 | `stock_hk_hist()` |
| `hk-min` | 港股分钟K | `stock_hk_hist_min_em()` |
| `us` | 美股K线 | `stock_us_hist()` |
| `us-min` | 美股分钟K | `stock_us_hist_min_em()` |
| `index` | 指数历史 | `stock_zh_index_daily_em()` |

参数: `--code`, `--period`(daily/weekly/monthly/1/5/15/30/60), `--start`, `--end`, `--adjust`(qfq/hfq/"")

## 3. 财务数据 (stock/financial.py)

| 命令 | 说明 | AKShare 函数 |
|------|------|-------------|
| `profit` | 利润表 | `stock_profit_sheet_by_report_em()` |
| `balance` | 资产负债表 | `stock_balance_sheet_by_report_em()` |
| `cash-flow` | 现金流量表 | `stock_cash_flow_sheet_by_report_em()` |
| `abstract` | 同花顺财务摘要 | `stock_financial_abstract_ths()` |
| `indicator` | 东财财务指标 | `stock_financial_analysis_indicator_em()` |
| `report` | 业绩报表 | `stock_yjbb_em()` |
| `forecast` | 业绩预告 | `stock_yjyg_em()` |
| `quick-report` | 业绩快报 | `stock_yjkb_em()` |
| `dividend` | 分红配送 | `stock_fhps_em()` |
| `shareholders` | 股东户数 | `stock_zh_a_gdhs()` |
| `top10` | 十大股东 | `stock_gdfx_top_10_em()` |
| `top10-float` | 十大流通股东 | `stock_gdfx_free_top_10_em()` |
| `main-holders` | 主要股东(详细) | `stock_main_stock_holder()` |

## 4. 板块分析 (stock/board.py)

| 命令 | 说明 | AKShare 函数 |
|------|------|-------------|
| `industry-list` | 行业板块行情 | `stock_board_industry_name_em()` |
| `concept-list` | 概念板块行情 | `stock_board_concept_name_em()` |
| `industry-cons` | 行业成分股 | `stock_board_industry_cons_em()` |
| `concept-cons` | 概念成分股 | `stock_board_concept_cons_em()` |
| `industry-hist` | 行业板块K线 | `stock_board_industry_hist_em()` |
| `concept-hist` | 概念板块K线 | `stock_board_concept_hist_em()` |

## 5. 资金流向 (stock/fund_flow.py)

| 命令 | 说明 | AKShare 函数 |
|------|------|-------------|
| `individual` | 个股资金流 | `stock_individual_fund_flow()` |
| `individual-rank` | 个股资金排名 | `stock_individual_fund_flow_rank()` |
| `market` | 大盘资金流 | `stock_market_fund_flow()` |
| `main` | 主力资金流 | `stock_main_fund_flow()` |
| `industry` | 行业资金流 | `stock_fund_flow_industry()` |
| `concept` | 概念资金流 | `stock_fund_flow_concept()` |
| `sector-rank` | 板块资金排名 | `stock_sector_fund_flow_rank()` |
| `individual-hist` | 个股历史资金流 | `stock_fund_flow_individual()` |
| `sector-hist` | 板块历史资金流 | `stock_sector_fund_flow_hist()` |

## 6. 特殊数据 (stock/special.py) — 60+ 接口

### 龙虎榜
| 命令 | 说明 |
|------|------|
| `lhb-detail` | 龙虎榜详情 |
| `lhb-stock` | 个股龙虎榜 |
| `lhb-stat` | 龙虎榜统计 |
| `lhb-inst` | 机构统计 |
| `lhb-trader` | 营业部统计 |

### 涨跌停
| 命令 | 说明 |
|------|------|
| `zt-pool` | 涨停池 |
| `dt-pool` | 跌停池 |
| `zt-strong` | 强势股池 |
| `zt-previous` | 昨日涨停 |
| `zt-sub-new` | 次新股涨停 |
| `zt-zbgc` | 涨停不打开 |

### 融资融券
| 命令 | 说明 |
|------|------|
| `margin-sse` | 沪市融资融券 |
| `margin-szse` | 深市融资融券 |
| `margin-detail-sse` | 沪市两融明细 |
| `margin-ratio` | 两融余额占比 |

### 股权质押
| 命令 | 说明 |
|------|------|
| `pledge-profile` | 质押市场概况 |
| `pledge-ratio` | 上市公司质押比例 |
| `pledge-detail` | 个股质押明细 |
| `pledge-bank` | 银行质押分布 |
| `pledge-company` | 券商质押分布 |
| `pledge-industry` | 行业质押数据 |

### 商誉
| 命令 | 说明 |
|------|------|
| `goodwill-profile` | 商誉市场概况 |
| `goodwill-expected` | 减值预期明细 |
| `goodwill-detail` | 个股减值明细 |
| `goodwill-stock` | 个股商誉明细 |
| `goodwill-industry` | 行业商誉 |

### 机构调研
| 命令 | 说明 |
|------|------|
| `inst-research-stat` | 调研统计 |
| `inst-research-detail` | 个股调研详情 |
| `analyst-rank` | 分析师排名 |
| `inst-recommend` | 机构推荐 |

### 大宗交易
| 命令 | 说明 |
|------|------|
| `block-daily` | 每日统计 |
| `block-detail` | 每日明细 |
| `block-sector` | 行业成交统计 |
| `block-sector-rank` | 营业部排行 |

### IPO / 解禁 / 沪深港通 / 估值 / 研报 / 公告 / 可转债
详见 SKILL.md 使用示例

---

## 7. 指数数据 (index/data.py)

| 命令 | 说明 | AKShare 函数 |
|------|------|-------------|
| `spot` | 指数实时 | `stock_zh_index_spot_em()` |
| `daily` | 指数历史 | `stock_zh_index_daily_em()` |
| `cons` | 成分股 | `index_stock_cons_csindex()` |
| `cons-weight` | 成分股权重 | `index_stock_cons_weight_csindex()` |
| `info` | 指数列表 | `index_stock_info()` |
| `sw` | 申万行业指数 | `sw_index_third_info()` |

## 8. 宏观数据 (macro/data.py)

### 中国 (cn)
gdp, cpi, cpi-monthly, ppi, pmi, cx-pmi, non-pmi, m2, fx-reserves,
exports, imports, trade, industrial, unemployment, shibor, lpr, rmb,
gdp-quarter, cpi-data, ppi-data, pmi-data, social-finance

### 美国 (us)
gdp, cpi, cpi-yoy, core-cpi, non-farm, unemployment, ppi, pmi, ism-pmi,
retail, trade, interest-rate, initial-jobless, eia-crude

### 全球 (global)
gold-etf, silver-etf, opec, cftc, leverage, fx-sentiment

## 9. 市场总貌 (market/summary.py)

| 命令 | 说明 | AKShare 函数 |
|------|------|-------------|
| `sse` | 上交所总貌 | `stock_sse_summary()` |
| `szse` | 深交所总貌 | `stock_szse_summary()` |
| `sse-daily` | 上交所每日概况 | `stock_sse_deal_daily()` |
| `szse-area` | 地区交易排序 | `stock_szse_area_summary()` |
| `szse-sector` | 行业成交 | `stock_szse_sector_summary()` |

---

## AKShare 全部股票接口速查 (617个)

完整接口列表请参考 AKShare 官方文档：
- 文档: https://akshare.akfamily.xyz/data/stock/stock.html
- GitHub: https://github.com/akfamily/akshare
