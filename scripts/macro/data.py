#!/usr/bin/env python3
"""
Macro economic data - China and global.
Usage: python macro.py <indicator> [--json]
"""
import sys, os
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _SCRIPT_DIR)  # for common.py in same dir
sys.path.insert(0, os.path.join(_SCRIPT_DIR, '..'))  # for common.py in parent


import sys
import argparse
import akshare as ak
from common import output, error, info, timeout


# ── China Macro ──────────────────────────────────────────────────────────────

INDICATORS_CN = {
    "gdp": ("GDP 年率", lambda: ak.macro_china_gdp_yearly()),
    "cpi": ("CPI 年率", lambda: ak.macro_china_cpi_yearly()),
    "cpi-monthly": ("CPI 月率", lambda: ak.macro_china_cpi_monthly()),
    "ppi": ("PPI 年率", lambda: ak.macro_china_ppi_yearly()),
    "pmi": ("官方制造业 PMI", lambda: ak.macro_china_pmi_yearly()),
    "cx-pmi": ("财新制造业 PMI", lambda: ak.macro_china_cx_pmi_yearly()),
    "non-pmi": ("非制造业 PMI", lambda: ak.macro_china_non_man_pmi()),
    "m2": ("M2 货币供应年率", lambda: ak.macro_china_m2_yearly()),
    "fx-reserves": ("外汇储备", lambda: ak.macro_china_fx_reserves_yearly()),
    "exports": ("出口年率", lambda: ak.macro_china_exports_yoy()),
    "imports": ("进口年率", lambda: ak.macro_china_imports_yoy()),
    "trade": ("贸易帐", lambda: ak.macro_china_trade_balance()),
    "industrial": ("工业增加值年率", lambda: ak.macro_china_industrial_production_yoy()),
    "unemployment": ("城镇调查失业率", lambda: ak.macro_china_urban_unemployment()),
    "shibor": ("上海银行间同业拆借", lambda: ak.macro_china_shibor_all()),
    "lpr": ("贷款报价利率 LPR", lambda: ak.macro_china_lpr()),
    "rmb": ("人民币汇率中间价", lambda: ak.macro_china_rmb()),
    "gdp-quarter": ("GDP 季度", lambda: ak.macro_china_gdp()),
    "cpi-data": ("CPI 数据", lambda: ak.macro_china_cpi()),
    "ppi-data": ("PPI 数据", lambda: ak.macro_china_ppi()),
    "pmi-data": ("PMI 数据", lambda: ak.macro_china_pmi()),
    "social-finance": ("社会融资规模", lambda: ak.macro_china_shrzgm()),
}

# ── US Macro ─────────────────────────────────────────────────────────────────

INDICATORS_US = {
    "gdp": ("美国 GDP", lambda: ak.macro_usa_gdp_monthly()),
    "cpi": ("美国 CPI 月率", lambda: ak.macro_usa_cpi_monthly()),
    "cpi-yoy": ("美国 CPI 年率", lambda: ak.macro_usa_cpi_yoy()),
    "core-cpi": ("美国核心 CPI", lambda: ak.macro_usa_core_cpi_monthly()),
    "non-farm": ("非农就业", lambda: ak.macro_usa_non_farm()),
    "unemployment": ("失业率", lambda: ak.macro_usa_unemployment_rate()),
    "ppi": ("PPI", lambda: ak.macro_usa_ppi()),
    "pmi": ("制造业 PMI", lambda: ak.macro_usa_pmi()),
    "ism-pmi": ("ISM 制造业 PMI", lambda: ak.macro_usa_ism_pmi()),
    "retail": ("零售销售", lambda: ak.macro_usa_retail_sales()),
    "trade": ("贸易帐", lambda: ak.macro_usa_trade_balance()),
    "interest-rate": ("利率决议", lambda: ak.macro_bank_usa_interest_rate()),
    "initial-jobless": ("初请失业金", lambda: ak.macro_usa_initial_jobless()),
    "eia-crude": ("EIA 原油库存", lambda: ak.macro_usa_eia_crude_rate()),
}

# ── Global Macro ─────────────────────────────────────────────────────────────

INDICATORS_GLOBAL = {
    "gold-etf": ("全球最大黄金 ETF 持仓", lambda: ak.macro_cons_gold()),
    "silver-etf": ("全球最大白银 ETF 持仓", lambda: ak.macro_cons_silver()),
    "opec": ("OPEC 报告", lambda: ak.macro_cons_opec_month()),
    "cftc": ("CFTC 持仓报告", lambda: ak.macro_usa_cftc_nc_holding()),
    "leverage": ("中国宏观杠杆率", lambda: ak.macro_cnbs()),
    "fx-sentiment": ("货币投机情绪", lambda: ak.macro_fx_sentiment()),
}


@timeout(60)
def run_indicator(category, indicator, as_json=False):
    """Run a macro indicator query."""
    tables = {"cn": INDICATORS_CN, "us": INDICATORS_US, "global": INDICATORS_GLOBAL}
    table = tables.get(category)
    if not table:
        error(f"Unknown category: {category}")

    if indicator not in table:
        print(f"Available indicators for {category}:", file=sys.stderr)
        for k, (name, _) in table.items():
            print(f"  {k}: {name}", file=sys.stderr)
        error(f"Unknown indicator: {indicator}")

    name, func = table[indicator]
    info(f"Fetching: {name}")
    df = func()
    output(df, as_json=as_json)


def main():
    parser = argparse.ArgumentParser(description="Macro economic data")
    parser.add_argument("category", choices=["cn", "us", "global", "list"])
    parser.add_argument("indicator", nargs="?", default="", help="Indicator name")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.category == "list":
        for cat, table in [("cn", INDICATORS_CN), ("us", INDICATORS_US), ("global", INDICATORS_GLOBAL)]:
            print(f"\n=== {cat.upper()} ===")
            for k, (name, _) in table.items():
                print(f"  {k}: {name}")
        return

    if not args.indicator:
        error("indicator is required (use 'list' to see available)")

    run_indicator(args.category, args.indicator, args.json)


if __name__ == "__main__":
    main()
