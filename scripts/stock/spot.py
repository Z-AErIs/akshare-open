#!/usr/bin/env python3
"""
A-share, HK stock, and US stock real-time quotes via AKShare.
Usage: python spot.py <market> [--code CODE] [--json]
  market: a-all, sh, sz, bj, hk, us, ah, index
"""
import sys, os
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _SCRIPT_DIR)  # for common.py in same dir
sys.path.insert(0, os.path.join(_SCRIPT_DIR, '..'))  # for common.py in parent


import sys
import argparse
import akshare as ak
from common import output, error, info, timeout


@timeout(90)
def spot_a_all(as_json=False):
    """全市场 A 股实时行情 (~70s, 5800+ rows)"""
    info("Fetching all A-share spots (~70s)...")
    df = ak.stock_zh_a_spot_em()
    output(df, as_json=as_json, max_rows=30)


@timeout(40)
def spot_sh(as_json=False):
    """沪 A 股实时行情"""
    df = ak.stock_sh_a_spot_em()
    output(df, as_json=as_json, max_rows=30)


@timeout(40)
def spot_sz(as_json=False):
    """深 A 股实时行情"""
    df = ak.stock_sz_a_spot_em()
    output(df, as_json=as_json, max_rows=30)


@timeout(40)
def spot_bj(as_json=False):
    """北证 A 股实时行情"""
    df = ak.stock_bj_a_spot_em()
    output(df, as_json=as_json, max_rows=30)


@timeout(40)
def spot_kc(as_json=False):
    """科创板实时行情"""
    df = ak.stock_kc_a_spot_em()
    output(df, as_json=as_json, max_rows=30)


@timeout(40)
def spot_cy(as_json=False):
    """创业板实时行情"""
    df = ak.stock_cy_a_spot_em()
    output(df, as_json=as_json, max_rows=30)


@timeout(40)
def spot_new(as_json=False):
    """新股实时行情"""
    df = ak.stock_new_a_spot_em()
    output(df, as_json=as_json, max_rows=30)


@timeout(60)
def spot_hk(as_json=False):
    """港股实时行情"""
    info("Fetching HK stock spots (~30s)...")
    df = ak.stock_hk_spot_em()
    output(df, as_json=as_json, max_rows=30)


@timeout(60)
def spot_us(as_json=False):
    """美股实时行情"""
    info("Fetching US stock spots (~30s)...")
    df = ak.stock_us_spot_em()
    output(df, as_json=as_json, max_rows=30)


@timeout(30)
def spot_ah(as_json=False):
    """A+H 股实时行情"""
    df = ak.stock_zh_ah_spot_em()
    output(df, as_json=as_json, max_rows=30)


@timeout(15)
def spot_index(as_json=False):
    """A 股指数实时行情"""
    df = ak.stock_zh_index_spot_em()
    output(df, as_json=as_json, max_rows=30)


@timeout(10)
def stock_info(code: str, as_json=False):
    """个股基本信息 + 实时快照"""
    df = ak.stock_individual_info_em(symbol=code)
    output(df, as_json=as_json)


@timeout(10)
def stock_bid_ask(code: str, as_json=False):
    """个股五档盘口"""
    df = ak.stock_bid_ask_em(symbol=code)
    output(df, as_json=as_json)


@timeout(10)
def stock_info_xq(code: str, as_json=False):
    """雪球个股公司概况"""
    # Need full code format like SH600519
    df = ak.stock_individual_basic_info_xq(symbol=code)
    output(df, as_json=as_json)


def main():
    parser = argparse.ArgumentParser(description="Stock real-time quotes")
    parser.add_argument("market", choices=[
        "a-all", "sh", "sz", "bj", "kc", "cy", "new",
        "hk", "us", "ah", "index",
        "info", "bid-ask", "info-xq"
    ])
    parser.add_argument("--code", help="Stock code for info/bid-ask")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    handlers = {
        "a-all": lambda: spot_a_all(args.json),
        "sh": lambda: spot_sh(args.json),
        "sz": lambda: spot_sz(args.json),
        "bj": lambda: spot_bj(args.json),
        "kc": lambda: spot_kc(args.json),
        "cy": lambda: spot_cy(args.json),
        "new": lambda: spot_new(args.json),
        "hk": lambda: spot_hk(args.json),
        "us": lambda: spot_us(args.json),
        "ah": lambda: spot_ah(args.json),
        "index": lambda: spot_index(args.json),
        "info": lambda: stock_info(args.code, args.json),
        "bid-ask": lambda: stock_bid_ask(args.code, args.json),
        "info-xq": lambda: stock_info_xq(args.code, args.json),
    }

    if args.market in ("info", "bid-ask", "info-xq") and not args.code:
        error("--code is required for info/bid-ask/info-xq")

    handlers[args.market]()


if __name__ == "__main__":
    main()
