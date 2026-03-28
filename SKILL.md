---
name: akshare
description: >
  A股全覆盖 + 港股 + 美股 + 指数 + 财务 + 宏观经济数据。
  免费、无需 API Key、Python 原生。支持实时行情、历史K线、板块分析、资金流向、
  财务三表、股东研究、龙虎榜、涨跌停、融资融券、宏观数据等。
  提到A股、港股行情、财务报表、财报、宏观、GDP、CPI、PMI、板块、资金流、
  龙虎榜、涨跌停、融资融券、IPO、解禁、研报 时自动使用。
allowed-tools: Bash Read Write Edit
---

# AKShare 投研数据助手

基于 [AKShare](https://github.com/akfamily/akshare) 的开源财经数据接口库。
**免费、无需 API Key、数据来自东财/新浪/同花顺/巨潮等公开数据源。**

## 核心特性

- **A 股全覆盖**：沪深京 5800+ 只股票，含科创板、创业板、北证
- **港股/美股**：实时行情 + 历史 K 线
- **财务数据**：三大报表、业绩预告/快报/报告、分红配送、股东研究
- **板块分析**：行业/概念板块行情 + 成分股 + 资金流向
- **宏观数据**：中国 GDP/CPI/PMI/M2/社融、美国非农/CPI/利率
- **特殊数据**：龙虎榜、涨跌停、融资融券、限售解禁、研报

## 前提条件

```bash
pip install akshare --upgrade
```

Python 3.9+（64 位），推荐 3.11+。

## 数据路由建议

本工具为纯数据获取工具，不限定与特定交易系统搭配。
以下为常见搭配参考（非强制）：

| 场景 | 推荐数据源 |
|------|-----------|
| A 股全覆盖研究 | 本工具（AKShare） |
| 港股实时深度行情 | 可搭配支持 LV2 的行情系统 |
| 交易执行 | 可搭配支持下单的交易系统 |
| 宏观/财务分析 | 本工具（AKShare） |

## 脚本目录

```
scripts/
├── common.py                    # 公共工具（超时、重试、输出格式化）
├── stock/
│   ├── spot.py                  # 实时行情（A/HK/US/个股/盘口）
│   ├── hist.py                  # 历史K线（日/周/月/分钟）
│   ├── financial.py             # 财务数据（三表/业绩/分红/股东）
│   ├── board.py                 # 板块分析（行业/概念）
│   ├── fund_flow.py             # 资金流向（个股/板块/大盘）
│   └── special.py               # 特殊数据（龙虎榜/涨跌停/两融/IPO/研报）
├── index/
│   └── data.py                  # 指数数据（行情/历史/成分股）
├── macro/
│   └── data.py                  # 宏观数据（中美经济指标）
└── market/
    └── summary.py               # 市场总貌（交易所概况/行业成交）
```

## 使用方式

所有脚本均支持 `--json` 参数输出 JSON 格式，便于程序解析。
脚本路径基于 skill 目录，执行时请先确认脚本文件存在。

---

## 一、实时行情

### A 股全市场行情（较慢 ~70s）

```bash
python scripts/stock/spot.py a-all [--json]           # 沪深京全部A股 (~70s)
python scripts/stock/spot.py sh [--json]               # 沪A股 (~28s)
python scripts/stock/spot.py sz [--json]               # 深A股
python scripts/stock/spot.py bj [--json]               # 北证A股
python scripts/stock/spot.py kc [--json]               # 科创板
python scripts/stock/spot.py cy [--json]               # 创业板
python scripts/stock/spot.py new [--json]              # 新股
```

### 个股详情

```bash
python scripts/stock/spot.py info --code 000001 [--json]        # 个股基本信息
python scripts/stock/spot.py bid-ask --code 000001 [--json]     # 五档盘口
```

### 港股/美股

```bash
python scripts/stock/spot.py hk [--json]               # 港股实时 (~30s)
python scripts/stock/spot.py us [--json]               # 美股实时 (~30s)
python scripts/stock/spot.py ah [--json]               # A+H股对比
```

### 指数行情

```bash
python scripts/stock/spot.py index [--json]            # A股指数实时
```

> **性能提示**：全市场行情接口较慢（>60s）。查询个股必须用个股接口，
> 不要用全市场接口筛选。个股接口通常 3-5 秒返回。

---

## 二、历史 K 线

### A 股历史 K 线

```bash
# 日/周/月 K 线
python scripts/stock/hist.py a --code 000001 --period daily --start 20250101 --end 20250328 --adjust qfq [--json]

# 分钟 K 线 (1/5/15/30/60)
python scripts/stock/hist.py a-min --code 000001 --period 5 --start "2025-03-27 09:30:00" --end "2025-03-27 15:00:00" [--json]
```

### 港股/美股历史

```bash
python scripts/stock/hist.py hk --code 00700 --period daily --start 20250101 --end 20250328 [--json]
python scripts/stock/hist.py us --code AAPL --period daily --start 20250101 --end 20250328 [--json]
python scripts/stock/hist.py hk-min --code 00700 --period 1 --start "2025-03-27 09:30:00" --end "2025-03-27 16:00:00" [--json]
```

### 指数历史

```bash
python scripts/stock/hist.py index --code sh000001 [--json]     # 上证指数
```

---

## 三、财务数据

### 三大报表

```bash
python scripts/stock/financial.py profit --code 000001 [--json]        # 利润表
python scripts/stock/financial.py balance --code 000001 [--json]       # 资产负债表
python scripts/stock/financial.py cash-flow --code 000001 [--json]     # 现金流量表
python scripts/stock/financial.py abstract --code 000001 [--json]      # 同花顺财务摘要
python scripts/stock/financial.py indicator --code 000001 [--json]     # 东财财务指标
```

### 业绩数据

```bash
python scripts/stock/financial.py report --date 20240930 [--json]      # 业绩报表
python scripts/stock/financial.py forecast --date 20240930 [--json]    # 业绩预告
python scripts/stock/financial.py quick-report --date 20240930 [--json] # 业绩快报
python scripts/stock/financial.py dividend --code 000001 [--json]      # 分红配送
```

### 股东研究

```bash
python scripts/stock/financial.py shareholders --code 000001 [--json]        # 股东户数
python scripts/stock/financial.py top10 --code 000001 [--json]               # 十大股东
python scripts/stock/financial.py top10-float --code 000001 [--json]         # 十大流通股东
python scripts/stock/financial.py main-holders --code 000001 [--json]        # 主要股东（详细）
```

---

## 四、板块分析

```bash
python scripts/stock/board.py industry-list [--json]                          # 行业板块行情
python scripts/stock/board.py concept-list [--json]                           # 概念板块行情
python scripts/stock/board.py industry-cons --board 银行 [--json]             # 行业成分股
python scripts/stock/board.py concept-cons --board 人工智能 [--json]          # 概念成分股
python scripts/stock/board.py industry-hist --board 银行 --start 20250101 [--json]  # 行业板块K线
python scripts/stock/board.py concept-hist --board 人工智能 --start 20250101 [--json]  # 概念板块K线
```

---

## 五、资金流向

```bash
python scripts/stock/fund_flow.py individual --code 000001 --market sz [--json]   # 个股资金流
python scripts/stock/fund_flow.py individual-rank --indicator 今日 [--json]        # 个股排名
python scripts/stock/fund_flow.py market [--json]                                  # 大盘资金流
python scripts/stock/fund_flow.py main [--json]                                    # 主力资金流
python scripts/stock/fund_flow.py industry --indicator 今日 [--json]               # 行业资金流
python scripts/stock/fund_flow.py concept --indicator 今日 [--json]                # 概念资金流
python scripts/stock/fund_flow.py sector-rank --indicator 今日 [--json]            # 板块排名
python scripts/stock/fund_flow.py individual-hist --code 000001 --market sz [--json]  # 个股历史
python scripts/stock/fund_flow.py sector-hist --board 银行 [--json]                # 板块历史
```

---

## 六、特殊数据

### 龙虎榜

```bash
python scripts/stock/special.py lhb-detail --start 20250320 --end 20250328 [--json]
python scripts/stock/special.py lhb-stock --code 000001 [--json]
python scripts/stock/special.py lhb-stat [--json]
```

### 涨跌停

```bash
python scripts/stock/special.py zt-pool --date 20250328 [--json]     # 涨停池
python scripts/stock/special.py dt-pool --date 20250328 [--json]     # 跌停池
python scripts/stock/special.py zt-strong --date 20250328 [--json]   # 强势股池
python scripts/stock/special.py zt-previous --date 20250328 [--json] # 昨日涨停
```

### 融资融券

```bash
python scripts/stock/special.py margin-sse --start 20250301 --end 20250328 [--json]
python scripts/stock/special.py margin-szse --date 20250301 [--json]
python scripts/stock/special.py margin-ratio [--json]
```

### IPO / 解禁

```bash
python scripts/stock/special.py ipo-declare [--json]
python scripts/stock/special.py ipo-list [--json]
python scripts/stock/special.py restricted-release [--json]
```

### 沪深港通

```bash
python scripts/stock/special.py hsgt-hist --symbol 沪股通 [--json]
python scripts/stock/special.py hsgt-summary [--json]
```

### 估值

```bash
python scripts/stock/special.py all-pb [--json]     # 全A市净率 (~30s)
python scripts/stock/special.py all-pe [--json]     # 全A市盈率 (~30s)
```

### 研报 & 新闻

```bash
python scripts/stock/special.py research-report [--json]
python scripts/stock/special.py stock-news --code 000001 [--json]
python scripts/stock/special.py hot-rank [--json]
```

---

## 七、指数数据

```bash
python scripts/index/data.py spot [--json]                                # 指数实时
python scripts/index/data.py daily --code sh000001 [--json]               # 指数历史
python scripts/index/data.py cons --code 000300 [--json]                  # 沪深300成分股
python scripts/index/data.py cons-weight --code 000300 [--json]           # 成分股权重
python scripts/index/data.py info [--json]                                # 所有指数列表
python scripts/index/data.py sw [--json]                                  # 申万行业指数
```

---

## 八、宏观数据

```bash
# 查看所有可用指标
python scripts/macro/data.py list

# 中国宏观
python scripts/macro/data.py cn gdp [--json]              # GDP
python scripts/macro/data.py cn cpi [--json]              # CPI
python scripts/macro/data.py cn ppi [--json]              # PPI
python scripts/macro/data.py cn pmi [--json]              # PMI
python scripts/macro/data.py cn m2 [--json]               # M2
python scripts/macro/data.py cn lpr [--json]              # LPR
python scripts/macro/data.py cn social-finance [--json]   # 社融
python scripts/macro/data.py cn shibor [--json]           # Shibor

# 美国宏观
python scripts/macro/data.py us non-farm [--json]         # 非农
python scripts/macro/data.py us cpi [--json]              # CPI
python scripts/macro/data.py us interest-rate [--json]    # 利率决议
python scripts/macro/data.py us ism-pmi [--json]          # ISM PMI

# 全球
python scripts/macro/data.py global gold-etf [--json]     # 黄金 ETF 持仓
python scripts/macro/data.py global silver-etf [--json]   # 白银 ETF 持仓
python scripts/macro/data.py global leverage [--json]     # 中国宏观杠杆率
```

---

## 九、市场总貌

```bash
python scripts/market/summary.py sse [--json]                              # 上交所总貌
python scripts/market/summary.py szse --date 20250328 [--json]             # 深交所总貌
python scripts/market/summary.py sse-daily --date 20250328 [--json]        # 上交所每日概况
python scripts/market/summary.py szse-area --date 202503 [--json]          # 地区交易排序
python scripts/market/summary.py szse-sector --date 202503 [--json]        # 行业成交
```

---

## 常见股票代码速查

| 名称 | 代码 | 市场 |
|------|------|------|
| 平安银行 | 000001 | sz |
| 贵州茅台 | 600519 | sh |
| 宁德时代 | 300750 | sz |
| 比亚迪 | 002594 | sz |
| 招商银行 | 600036 | sh |
| 腾讯控股 | 00700 | hk |
| 阿里巴巴 | 09988 | hk |
| 苹果 | AAPL | us |
| 沪深300指数 | 000300 | index |

## 日期格式

- 日线/周线/月线：`YYYYMMDD`（如 `20250101`）
- 分钟线：`YYYY-MM-DD HH:MM:SS`（如 `2025-03-27 09:30:00`）
- 获取当日可用 `datetime.now().strftime("%Y%m%d")`

## 性能提示

- **全市场行情**（`a-all`、`sh`、`sz` 等）较慢（20-70s），不要用于频繁轮询
- **个股接口**（`info`、`bid-ask`、`hist`）通常 3-10s，是日常使用的主力
- **批量查询**建议先用 `a-all` 拉取全量快照到本地，再在本地筛选
- **实时行情**为延迟数据（通常延迟 15 分钟），非 Level 2 实时
- 数据仅供学术研究，不构成投资建议

## 错误处理

| 错误 | 解决 |
|------|------|
| `Connection timeout` | 网络问题，重试或检查代理 |
| `KeyError` / `Column mismatch` | 东财改版，升级 AKShare：`pip install akshare --upgrade` |
| `No data returned` | 股票代码格式错误，或非交易日无数据 |
| `Rate limit` | 请求太频繁，加间隔重试 |
| 脚本超时 | 使用 `--json` 减少输出开销，或检查网络 |

## 维护提示

AKShare 数据来自网页抓取，接口可能因目标网站改版而失效。
**建议定期升级**：`pip install akshare --upgrade`

当前适配版本：AKShare 1.18.x
