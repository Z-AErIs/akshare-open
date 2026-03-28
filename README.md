# AKShare Open 🔍📈

[AKShare](https://github.com/akfamily/akshare) 的 Agent Skill 封装，专为 AI Agent（[OpenClaw](https://github.com/openclaw/openclaw) / Claude Code / Cursor 等）设计的 **A 股 + 港股 + 美股**投研数据工具。

> **免费 · 无需 API Key · 开箱即用 · 150+ 接口**

---

## 中文

### ✨ 特性

- **A 股全覆盖**：沪深京 5800+ 只股票，含科创板、创业板、北证
- **港股 / 美股**：实时行情 + 历史 K 线
- **财务数据**：三大报表、业绩预告 / 快报、分红配送、股东研究
- **板块分析**：行业 / 概念板块行情 + 成分股 + 资金流向
- **宏观数据**：中国 GDP / CPI / PMI / M2 / 社融、美国非农 / CPI / 利率
- **特殊数据**：龙虎榜、涨跌停、融资融券、限售解禁、股权质押、商誉、大宗交易、可转债、研报
- **JSON 输出**：所有脚本支持 `--json`，方便 Agent 程序化解析
- **超时重试**：内置网络超时和自动重试机制

### 📦 安装

#### 1. 安装 AKShare

```bash
pip install akshare --upgrade
```

Python 3.9+（64 位），推荐 3.11+。

#### 2. 安装 Skill

**方式一：OpenClaw**

```bash
git clone https://github.com/Z-AErIs/akshare-open.git ~/.openclaw/skills/akshare
```

**方式二：Claude Code**

```bash
git clone https://github.com/Z-AErIs/akshare-open.git .claude/skills/akshare
```

**方式三：手动下载**

下载本仓库，将 `SKILL.md` 和 `scripts/` 目录放到对应的 skills 目录。

### 🚀 快速开始

```bash
# 查看贵州茅台基本信息
python scripts/stock/spot.py info --code 600519

# 获取平安银行日 K 线（前复权）
python scripts/stock/hist.py a --code 000001 --period daily --start 20250101 --end 20250328 --adjust qfq

# 查看行业板块行情
python scripts/stock/board.py industry-list

# 查询 GDP 数据
python scripts/macro/data.py cn gdp

# JSON 输出
python scripts/stock/spot.py info --code 600519 --json
```

### 📂 脚本结构

```
scripts/
├── common.py                    # 公共工具（超时、重试、输出格式化）
├── stock/
│   ├── spot.py                  # 实时行情（A/HK/US/个股/盘口）
│   ├── hist.py                  # 历史K线（日/周/月/分钟）
│   ├── financial.py             # 财务数据（三表/业绩/分红/股东）
│   ├── board.py                 # 板块分析（行业/概念）
│   ├── fund_flow.py             # 资金流向（个股/板块/大盘）
│   └── special.py               # 特殊数据（60+接口：龙虎榜/涨跌停/两融/质押/商誉/大宗/可转债…）
├── index/
│   └── data.py                  # 指数数据（行情/历史/成分股）
├── macro/
│   └── data.py                  # 宏观数据（中美经济指标 30+）
└── market/
    └── summary.py               # 市场总貌（交易所概况/行业成交）
```

### 📖 文档

- [SKILL.md](SKILL.md) — 完整使用文档（所有接口用法和示例）
- [references/api-reference.md](references/api-reference.md) — API 参考手册（150+ 接口速查）

### 🤝 与其他工具配合

本工具为纯数据获取工具，不限定与特定交易系统搭配：

| 场景 | 建议 |
|------|------|
| A 股全覆盖研究 | 本工具（AKShare） |
| 港股实时深度行情 | 可搭配支持 LV2 的行情系统 |
| 交易执行 | 可搭配支持下单的交易系统 |
| 宏观 / 财务分析 | 本工具（AKShare） |

### ⚠️ 注意事项

- 数据仅供学术研究，不构成投资建议
- 全市场行情接口较慢（20-70s），查询个股请用个股接口（3-10s）
- 数据来自网页抓取，建议定期升级 AKShare：`pip install akshare --upgrade`
- 实时行情通常有 15 分钟延迟，非 Level 2 实时

---

## English

### Features

- **A-Share Full Coverage**: 5800+ stocks across Shanghai, Shenzhen, and Beijing exchanges
- **HK / US Stocks**: Real-time quotes + historical K-lines
- **Financial Data**: Balance sheet, income statement, cash flow, earnings forecasts, dividends
- **Sector Analysis**: Industry/concept boards, constituents, fund flows
- **Macro Data**: China GDP/CPI/PMI/M2, US Non-farm/CPI/Interest Rates
- **Special Data**: Dragon list, limit up/down, margin trading, IPO, pledge, goodwill, block trades, convertibles
- **JSON Output**: All scripts support `--json` for programmatic parsing
- **Timeout & Retry**: Built-in network resilience

### Installation

```bash
pip install akshare --upgrade
git clone https://github.com/Z-AErIs/akshare-open.git ~/.openclaw/skills/akshare
```

### Quick Start

```bash
# Get stock info
python scripts/stock/spot.py info --code 600519

# Get historical K-line
python scripts/stock/hist.py a --code 000001 --period daily --start 20250101 --end 20250328 --adjust qfq

# Get industry boards
python scripts/stock/board.py industry-list

# Get China GDP
python scripts/macro/data.py cn gdp

# JSON output
python scripts/stock/spot.py info --code 600519 --json
```

### Documentation

- [SKILL.md](SKILL.md) — Full usage documentation
- [references/api-reference.md](references/api-reference.md) — API reference (150+ interfaces)

### Note

- Data is for academic research only, not investment advice
- Market-wide queries are slow (20-70s); use individual stock queries for speed
- Data sourced from web scraping; upgrade regularly: `pip install akshare --upgrade`

---

## 📄 License

[MIT](LICENSE)
