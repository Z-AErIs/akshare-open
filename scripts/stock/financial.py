#!/usr/bin/env python3
"""
Financial statements and fundamentals.
Usage: python financial.py <type> --code CODE [--indicator ...] [--json]
"""
import sys, os
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _SCRIPT_DIR)  # for common.py in same dir
sys.path.insert(0, os.path.join(_SCRIPT_DIR, '..'))  # for common.py in parent


import sys
import argparse
import akshare as ak
from common import output, error, info, timeout, validate_stock_code


def _full_code(code: str) -> str:
    """Convert short code to full format with SH/SZ prefix (e.g., 600519 -> SH600519)."""
    if "." in code:
        return code
    if code.startswith(("6", "9")):
        return f"SH{code}"
    elif code.startswith(("0", "3", "8")):
        return f"SZ{code}"
    return code


@timeout(60)
def profit_sheet(code, as_json=False):
    """利润表"""
    fc = _full_code(code)
    info(f"Using code: {fc}")
    df = ak.stock_profit_sheet_by_report_em(symbol=fc)
    output(df, as_json=as_json)


@timeout(60)
def balance_sheet(code, as_json=False):
    """资产负债表"""
    fc = _full_code(code)
    df = ak.stock_balance_sheet_by_report_em(symbol=fc)
    output(df, as_json=as_json)


@timeout(60)
def cash_flow(code, as_json=False):
    """现金流量表"""
    fc = _full_code(code)
    df = ak.stock_cash_flow_sheet_by_report_em(symbol=fc)
    output(df, as_json=as_json)


@timeout(30)
def financial_abstract(code, indicator="按报告期", as_json=False):
    """同花顺财务摘要"""
    df = ak.stock_financial_abstract_ths(symbol=code, indicator=indicator)
    output(df, as_json=as_json)


@timeout(30)
def financial_indicator(code, indicator="按报告期", as_json=False):
    """东财财务分析指标"""
    fc = _full_code(code)
    # Use format like "000001.SZ"
    short = fc.replace("SH", "").replace("SZ", "")
    suffix = "SZ" if code.startswith(("0", "3", "8")) else "SH"
    df = ak.stock_financial_analysis_indicator_em(symbol=f"{short}.{suffix}", indicator=indicator)
    output(df, as_json=as_json)


@timeout(30)
def performance_report(date, as_json=False):
    """业绩报表"""
    df = ak.stock_yjbb_em(date=date)
    output(df, as_json=as_json, max_rows=30)


@timeout(30)
def performance_forecast(date, as_json=False):
    """业绩预告"""
    df = ak.stock_yjyg_em(date=date)
    output(df, as_json=as_json, max_rows=30)


@timeout(30)
def performance_quick_report(date, as_json=False):
    """业绩快报"""
    df = ak.stock_yjkb_em(date=date)
    output(df, as_json=as_json, max_rows=30)


@timeout(30)
def dividend(code, as_json=False):
    """分红配送"""
    df = ak.stock_fhps_em(symbol=code)
    output(df, as_json=as_json)


@timeout(15)
def shareholders(code, as_json=False):
    """股东户数"""
    df = ak.stock_zh_a_gdhs(symbol=code)
    output(df, as_json=as_json)


@timeout(15)
def top10_shareholders(code, as_json=False):
    """十大股东"""
    df = ak.stock_gdfx_top_10_em(symbol=code)
    output(df, as_json=as_json)


@timeout(15)
def top10_float_shareholders(code, as_json=False):
    """十大流通股东"""
    df = ak.stock_gdfx_free_top_10_em(symbol=code)
    output(df, as_json=as_json)


@timeout(15)
def main_shareholders(code, as_json=False):
    """主要股东（详细）"""
    df = ak.stock_main_stock_holder(symbol=code)
    output(df, as_json=as_json)


def main():
    parser = argparse.ArgumentParser(description="Financial data")
    parser.add_argument("type", choices=[
        "profit", "balance", "cash-flow", "abstract", "indicator",
        "report", "forecast", "quick-report",
        "dividend", "shareholders", "top10", "top10-float", "main-holders"
    ])
    parser.add_argument("--code", help="Stock code")
    parser.add_argument("--date", help="Report date (YYYYMMDD)")
    parser.add_argument("--indicator", default="按报告期")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    needs_code = args.type not in ("report", "forecast", "quick-report")
    needs_date = args.type in ("report", "forecast", "quick-report")
    if needs_code and not args.code:
        error("--code is required")
    if needs_code and args.code:
        validate_stock_code(args.code)
    if needs_date and not args.date:
        error("--date is required")

    handlers = {
        "profit": lambda: profit_sheet(args.code, args.json),
        "balance": lambda: balance_sheet(args.code, args.json),
        "cash-flow": lambda: cash_flow(args.code, args.json),
        "abstract": lambda: financial_abstract(args.code, args.indicator, args.json),
        "indicator": lambda: financial_indicator(args.code, args.indicator, args.json),
        "report": lambda: performance_report(args.date, args.json),
        "forecast": lambda: performance_forecast(args.date, args.json),
        "quick-report": lambda: performance_quick_report(args.date, args.json),
        "dividend": lambda: dividend(args.code, args.json),
        "shareholders": lambda: shareholders(args.code, args.json),
        "top10": lambda: top10_shareholders(args.code, args.json),
        "top10-float": lambda: top10_float_shareholders(args.code, args.json),
        "main-holders": lambda: main_shareholders(args.code, args.json),
    }
    handlers[args.type]()


if __name__ == "__main__":
    main()
