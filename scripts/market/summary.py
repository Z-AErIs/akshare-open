#!/usr/bin/env python3
"""
Market overview: SSE/SZSE summary, trading days, sector performance.
Usage: python summary.py <type> [--date DATE] [--json]
"""
import sys, os
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _SCRIPT_DIR)  # for common.py in same dir
sys.path.insert(0, os.path.join(_SCRIPT_DIR, '..'))  # for common.py in parent


import sys
import argparse
import akshare as ak
from common import output, error, info, timeout


@timeout(15)
def sse_summary(as_json=False):
    """上交所股票数据总貌"""
    df = ak.stock_sse_summary()
    output(df, as_json=as_json)


@timeout(15)
def szse_summary(date, as_json=False):
    """深交所证券类别统计"""
    df = ak.stock_szse_summary(date=date)
    output(df, as_json=as_json)


@timeout(15)
def sse_deal_daily(date, as_json=False):
    """上交所每日概况"""
    df = ak.stock_sse_deal_daily(date=date)
    output(df, as_json=as_json)


@timeout(30)
def szse_area(date, as_json=False):
    """深交所地区交易排序"""
    df = ak.stock_szse_area_summary(date=date)
    output(df, as_json=as_json)


@timeout(30)
def szse_sector(symbol="当月", date="", as_json=False):
    """深交所股票行业成交"""
    df = ak.stock_szse_sector_summary(symbol=symbol, date=date)
    output(df, as_json=as_json)


def main():
    parser = argparse.ArgumentParser(description="Market overview")
    parser.add_argument("type", choices=["sse", "szse", "sse-daily", "szse-area", "szse-sector"])
    parser.add_argument("--date", default="", help="Date YYYYMMDD or YYYYMM")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    h = {
        "sse": lambda: sse_summary(args.json),
        "szse": lambda: szse_summary(args.date, args.json),
        "sse-daily": lambda: sse_deal_daily(args.date, args.json),
        "szse-area": lambda: szse_area(args.date, args.json),
        "szse-sector": lambda: szse_sector("当月", args.date, args.json),
    }
    h[args.type]()


if __name__ == "__main__":
    main()
