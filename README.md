# AKShare Open 🔍📈

[AKShare](https://github.com/akfamily/akshare) 的 Agent Skill 封装，专为 AI Agent（OpenClaw / Claude Code / Cursor 等）设计的 A 股 + 港股 + 美股投研数据工具。

## ✨ 特性

- **A 股全覆盖**：沪深京 5800+ 只股票，含科创板、创业板、北证
- **港股 / 美股**：实时行情 + 历史 K 线
- **财务数据**：三大报表、业绩预告 / 快报、分红配送、股东研究
- **板块分析**：行业 / 概念板块行情 + 成分股 + 资金流向
- **宏观数据**：中国 GDP / CPI / PMI / M2 / 社融、美国非农 / CPI / 利率
- **特殊数据**：龙虎榜、涨跌停、融资融券、限售解禁、研报
- **免费无 Key**：数据来自东财 / 新浪 / 同花顺 / 巨潮等公开数据源
- **JSON 输出**：所有脚本支持 `--json`，方便 Agent 程序化解析

## 📦 安装

### 1. 安装 AKShare

```bash
pip install akshare --upgrade
```

Python 3.9+（64 位），推荐 3.11+。

### 2. 安装 Skill

**方式一：OpenClaw**

```bash
# 克隆到 skills 目录
git clone https://github.com/YOUR_USERNAME/akshare-open.git ~/.openclaw/skills/akshare
```

**方式二：Claude Code**

```bash
# 克隆到 .claude/skills 目录
git clone https://github.com/YOUR_USERNAME/akshare-open.git .claude/skills/akshare
```

**方式三：手动**

下载本仓库，将 `SKILL.md` 和 `scripts/` 目录放到对应的 skills 目录。

## 🚀 快速开始

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

## 📂 脚本结构

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

## 📖 使用文档

详见 [SKILL.md](SKILL.md) — 包含所有接口的详细用法和示例。

## 🤝 与其他工具配合

本工具为纯数据获取工具，不限定与特定交易系统搭配。
以下为常见搭配参考：

| 场景 | 建议 |
|------|------|
| A 股全覆盖研究 | 本工具（AKShare） |
| 港股实时深度行情 | 可搭配支持 LV2 的行情系统 |
| 交易执行 | 可搭配支持下单的交易系统 |
| 宏观 / 财务分析 | 本工具（AKShare） |

## ⚠️ 注意事项

- 数据仅供学术研究，不构成投资建议
- 全市场行情接口较慢（20-70s），查询个股请用个股接口
- 数据来自网页抓取，建议定期升级 AKShare：`pip install akshare --upgrade`
- 实时行情通常有 15 分钟延迟，非 Level 2 实时

## 📄 License

MIT
