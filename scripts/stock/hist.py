#!/usr/bin/env python3
"""
Historical K-line data for A/HK/US stocks and indices.
Usage: python hist.py <type> --code CODE [--period daily] [--start 20250101] [--end 20250328] [--adjust qfq] [--json]
"""
import sys, os
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _SCRIPT_DIR)  # for common.py in same dir
sys.path.insert(0, os.path.join(_SCRIPT_DIR, '..'))  # for common.py in parent


import sys
import argparse
import akshare as ak
from common import output, error, info, timeout, validate_stock_code


@timeout(30)
def hist_a(code, period="daily", start="", end="", adjust="qfq", as_json=False):
    """A 股历史 K 线 (日/周/月)"""
    df = ak.stock_zh_a_hist(
        symbol=code, period=period,
        start_date=start, end_date=end, adjust=adjust
    )
    output(df, as_json=as_json, max_rows=30)


@timeout(30)
def hist_a_min(code, period="1", start="", end="", adjust="", as_json=False):
    """A 股分钟 K 线 (1/5/15/30/60)"""
    df = ak.stock_zh_a_hist_min_em(
        symbol=code, period=period,
        start_date=start, end_date=end, adjust=adjust
    )
    output(df, as_json=as_json, max_rows=50)


@timeout(30)
def hist_hk(code, period="daily", start="", end="", adjust="qfq", as_json=False):
    """港股历史 K 线"""
    df = ak.stock_hk_hist(
        symbol=code, period=period,
        start_date=start, end_date=end, adjust=adjust
    )
    output(df, as_json=as_json, max_rows=30)


@timeout(30)
def hist_hk_min(code, period="1", start="", end="", as_json=False):
    """港股分钟 K 线"""
    df = ak.stock_hk_hist_min_em(
        symbol=code, period=period,
        start_date=start, end_date=end
    )
    output(df, as_json=as_json, max_rows=50)


@timeout(30)
def hist_us(code, period="daily", start="", end="", adjust="qfq", as_json=False):
    """美股历史 K 线"""
    df = ak.stock_us_hist(
        symbol=code, period=period,
        start_date=start, end_date=end, adjust=adjust
    )
    output(df, as_json=as_json, max_rows=30)


@timeout(30)
def hist_us_min(code, period="1", start="", end="", as_json=False):
    """美股分钟 K 线"""
    df = ak.stock_us_hist_min_em(
        symbol=code, period=period,
        start_date=start, end_date=end
    )
    output(df, as_json=as_json, max_rows=50)


@timeout(30)
def hist_index(code, start="", end="", as_json=False):
    """股票指数历史行情 (东财)"""
    df = ak.stock_zh_index_daily_em(symbol=code)
    if start:
        df = df[df["date"] >= start]
    if end:
        df = df[df["date"] <= end]
    output(df, as_json=as_json, max_rows=30)


def main():
    parser = argparse.ArgumentParser(description="Historical K-line data")
    parser.add_argument("type", choices=["a", "a-min", "hk", "hk-min", "us", "us-min", "index"])
    parser.add_argument("--code", required=True)
    parser.add_argument("--period", default="daily")
    parser.add_argument("--start", default="")
    parser.add_argument("--end", default="")
    parser.add_argument("--adjust", default="qfq")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    validate_stock_code(args.code)

    handlers = {
        "a": lambda: hist_a(args.code, args.period, args.start, args.end, args.adjust, args.json),
        "a-min": lambda: hist_a_min(args.code, args.period, args.start, args.end, args.adjust, args.json),
        "hk": lambda: hist_hk(args.code, args.period, args.start, args.end, args.adjust, args.json),
        "hk-min": lambda: hist_hk_min(args.code, args.period, args.start, args.end, args.json),
        "us": lambda: hist_us(args.code, args.period, args.start, args.end, args.adjust, args.json),
        "us-min": lambda: hist_us_min(args.code, args.period, args.start, args.end, args.json),
        "index": lambda: hist_index(args.code, args.start, args.end, args.json),
    }
    handlers[args.type]()


if __name__ == "__main__":
    main()
