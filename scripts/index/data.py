#!/usr/bin/env python3
"""
Index data: quotes, history, constituents.
Usage: python index.py <action> [--code CODE] [--json]
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
def index_spot(as_json=False):
    """A 股指数实时行情"""
    df = ak.stock_zh_index_spot_em()
    output(df, as_json=as_json, max_rows=30)


@timeout(30)
def index_daily(code, start="", end="", as_json=False):
    """指数历史行情 (东财)"""
    df = ak.stock_zh_index_daily_em(symbol=code)
    if start:
        df = df[df["date"] >= start]
    if end:
        df = df[df["date"] <= end]
    output(df, as_json=as_json, max_rows=30)


@timeout(30)
def index_cons(code, as_json=False):
    """指数成分股 (中证)"""
    df = ak.index_stock_cons_csindex(symbol=code)
    output(df, as_json=as_json)


@timeout(30)
def index_cons_weight(code, as_json=False):
    """指数成分股权重 (中证)"""
    df = ak.index_stock_cons_weight_csindex(symbol=code)
    output(df, as_json=as_json)


@timeout(15)
def index_info(as_json=False):
    """所有可查询指数列表"""
    df = ak.index_stock_info()
    output(df, as_json=as_json, max_rows=50)


@timeout(30)
def sw_index(indicator="三级", as_json=False):
    """申万行业指数信息"""
    df = ak.sw_index_third_info()
    output(df, as_json=as_json, max_rows=30)


def main():
    parser = argparse.ArgumentParser(description="Index data")
    parser.add_argument("action", choices=["spot", "daily", "cons", "cons-weight", "info", "sw"])
    parser.add_argument("--code", help="Index code like sh000001 or 000300")
    parser.add_argument("--start", default="")
    parser.add_argument("--end", default="")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.action in ("daily", "cons", "cons-weight") and not args.code:
        error("--code is required")
    if args.code:
        validate_stock_code(args.code)

    h = {
        "spot": lambda: index_spot(args.json),
        "daily": lambda: index_daily(args.code, args.start, args.end, args.json),
        "cons": lambda: index_cons(args.code, args.json),
        "cons-weight": lambda: index_cons_weight(args.code, args.json),
        "info": lambda: index_info(args.json),
        "sw": lambda: sw_index("三级", args.json),
    }
    h[args.action]()


if __name__ == "__main__":
    main()
