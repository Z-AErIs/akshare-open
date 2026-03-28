#!/usr/bin/env python3
"""
Capital flow data - individual and sector fund flows.
Usage: python fund_flow.py <action> [--code CODE] [--market sz] [--indicator 今日] [--json]
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
def individual_flow(code, market="sz", as_json=False):
    """个股资金流向 (实时)"""
    df = ak.stock_individual_fund_flow(stock=code, market=market)
    output(df, as_json=as_json)


@timeout(30)
def individual_flow_rank(indicator="今日", as_json=False):
    """个股资金流向排名"""
    df = ak.stock_individual_fund_flow_rank(indicator=indicator)
    output(df, as_json=as_json, max_rows=30)


@timeout(15)
def market_flow(as_json=False):
    """大盘资金流向"""
    df = ak.stock_market_fund_flow()
    output(df, as_json=as_json)


@timeout(15)
def main_flow(as_json=False):
    """主力资金流向"""
    df = ak.stock_main_fund_flow()
    output(df, as_json=as_json)


@timeout(30)
def industry_flow(indicator="今日", as_json=False):
    """行业资金流向"""
    df = ak.stock_fund_flow_industry(indicator=indicator)
    output(df, as_json=as_json, max_rows=30)


@timeout(30)
def concept_flow(indicator="今日", as_json=False):
    """概念资金流向"""
    df = ak.stock_fund_flow_concept(indicator=indicator)
    output(df, as_json=as_json, max_rows=30)


@timeout(30)
def sector_flow_rank(indicator="今日", as_json=False):
    """板块资金流向排名"""
    df = ak.stock_sector_fund_flow_rank(indicator=indicator, sector_type="行业资金流")
    output(df, as_json=as_json, max_rows=30)


@timeout(30)
def individual_flow_hist(code, market="sz", as_json=False):
    """个股历史资金流向"""
    df = ak.stock_fund_flow_individual(stock=code, market=market)
    output(df, as_json=as_json, max_rows=30)


@timeout(30)
def sector_flow_hist(board, as_json=False):
    """板块历史资金流向"""
    df = ak.stock_sector_fund_flow_hist(symbol=board)
    output(df, as_json=as_json, max_rows=30)


def main():
    parser = argparse.ArgumentParser(description="Capital flow data")
    parser.add_argument("action", choices=[
        "individual", "individual-rank", "market", "main",
        "industry", "concept", "sector-rank",
        "individual-hist", "sector-hist"
    ])
    parser.add_argument("--code", help="Stock code")
    parser.add_argument("--market", default="sz", help="Market: sh/sz/bj")
    parser.add_argument("--indicator", default="今日")
    parser.add_argument("--board", help="Board name for sector-hist")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.action in ("individual", "individual-hist") and not args.code:
        error("--code is required")
    if args.action == "sector-hist" and not args.board:
        error("--board is required")

    handlers = {
        "individual": lambda: individual_flow(args.code, args.market, args.json),
        "individual-rank": lambda: individual_flow_rank(args.indicator, args.json),
        "market": lambda: market_flow(args.json),
        "main": lambda: main_flow(args.json),
        "industry": lambda: industry_flow(args.indicator, args.json),
        "concept": lambda: concept_flow(args.indicator, args.json),
        "sector-rank": lambda: sector_flow_rank(args.indicator, args.json),
        "individual-hist": lambda: individual_flow_hist(args.code, args.market, args.json),
        "sector-hist": lambda: sector_flow_hist(args.board, args.json),
    }
    handlers[args.action]()


if __name__ == "__main__":
    main()
