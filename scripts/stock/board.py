#!/usr/bin/env python3
"""
Sector/Board analysis - industry & concept boards.
Usage: python board.py <action> [--board NAME] [--json]
"""
import sys, os
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _SCRIPT_DIR)  # for common.py in same dir
sys.path.insert(0, os.path.join(_SCRIPT_DIR, '..'))  # for common.py in parent


import sys
import argparse
import akshare as ak
from common import output, error, info, timeout


@timeout(30)
def industry_list(as_json=False):
    """行业板块行情"""
    df = ak.stock_board_industry_name_em()
    output(df, as_json=as_json, max_rows=30)


@timeout(30)
def concept_list(as_json=False):
    """概念板块行情"""
    df = ak.stock_board_concept_name_em()
    output(df, as_json=as_json, max_rows=30)


@timeout(30)
def industry_cons(board, as_json=False):
    """行业板块成分股"""
    df = ak.stock_board_industry_cons_em(symbol=board)
    output(df, as_json=as_json)


@timeout(30)
def concept_cons(board, as_json=False):
    """概念板块成分股"""
    df = ak.stock_board_concept_cons_em(symbol=board)
    output(df, as_json=as_json)


@timeout(30)
def industry_hist(board, period="daily", start="", end="", as_json=False):
    """行业板块历史 K 线"""
    df = ak.stock_board_industry_hist_em(symbol=board, period=period, start_date=start, end_date=end)
    output(df, as_json=as_json, max_rows=30)


@timeout(30)
def concept_hist(board, period="daily", start="", end="", as_json=False):
    """概念板块历史 K 线"""
    df = ak.stock_board_concept_hist_em(symbol=board, period=period, start_date=start, end_date=end)
    output(df, as_json=as_json, max_rows=30)


@timeout(15)
def stock_boards(code, as_json=False):
    """个股所属板块"""
    df = ak.stock_board_concept_cons_em(symbol=code) if len(code) <= 6 else ak.stock_board_industry_cons_em(symbol=code)
    output(df, as_json=as_json)


def main():
    parser = argparse.ArgumentParser(description="Sector/Board analysis")
    parser.add_argument("action", choices=[
        "industry-list", "concept-list",
        "industry-cons", "concept-cons",
        "industry-hist", "concept-hist"
    ])
    parser.add_argument("--board", help="Board name")
    parser.add_argument("--start", default="")
    parser.add_argument("--end", default="")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    needs_board = "cons" in args.action or "hist" in args.action
    if needs_board and not args.board:
        error("--board is required")

    handlers = {
        "industry-list": lambda: industry_list(args.json),
        "concept-list": lambda: concept_list(args.json),
        "industry-cons": lambda: industry_cons(args.board, args.json),
        "concept-cons": lambda: concept_cons(args.board, args.json),
        "industry-hist": lambda: industry_hist(args.board, "daily", args.start, args.end, args.json),
        "concept-hist": lambda: concept_hist(args.board, "daily", args.start, args.end, args.json),
    }
    handlers[args.action]()


if __name__ == "__main__":
    main()
