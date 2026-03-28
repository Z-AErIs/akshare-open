#!/usr/bin/env python3
"""
Special data: dragon list, limit up/down, margin trading, IPO, restricted shares, etc.
Usage: python special.py <type> [--date DATE] [--code CODE] [--start START] [--end END] [--json]
"""
import sys, os
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _SCRIPT_DIR)  # for common.py in same dir
sys.path.insert(0, os.path.join(_SCRIPT_DIR, '..'))  # for common.py in parent


import sys
import argparse
import akshare as ak
from common import output, error, info, timeout


# ── Dragon List (龙虎榜) ──────────────────────────────────────────────────────

@timeout(30)
def lhb_detail(start, end, as_json=False):
    """龙虎榜详情"""
    df = ak.stock_lhb_detail_em(start_date=start, end_date=end)
    output(df, as_json=as_json, max_rows=30)


@timeout(30)
def lhb_stock(code, as_json=False):
    """个股龙虎榜"""
    df = ak.stock_lhb_stock_detail_em(symbol=code)
    output(df, as_json=as_json)


@timeout(30)
def lhb_stat(as_json=False):
    """龙虎榜统计"""
    df = ak.stock_lhb_stock_statistic_em()
    output(df, as_json=as_json, max_rows=30)


# ── Limit Up / Down (涨跌停) ─────────────────────────────────────────────────

@timeout(30)
def zt_pool(date, as_json=False):
    """涨停池"""
    df = ak.stock_zt_pool_em(date=date)
    output(df, as_json=as_json)


@timeout(30)
def dt_pool(date, as_json=False):
    """跌停池"""
    df = ak.stock_zt_pool_dtgc_em(date=date)
    output(df, as_json=as_json)


@timeout(30)
def zt_strong(date, as_json=False):
    """强势股池"""
    df = ak.stock_zt_pool_strong_em(date=date)
    output(df, as_json=as_json)


@timeout(30)
def zt_previous(date, as_json=False):
    """昨日涨停"""
    df = ak.stock_zt_pool_previous_em(date=date)
    output(df, as_json=as_json)


# ── Margin Trading (融资融券) ─────────────────────────────────────────────────

@timeout(30)
def margin_sse(start, end, as_json=False):
    """沪市融资融券"""
    df = ak.stock_margin_sse(start_date=start, end_date=end)
    output(df, as_json=as_json)


@timeout(30)
def margin_szse(date, as_json=False):
    """深市融资融券"""
    df = ak.stock_margin_szse(date=date)
    output(df, as_json=as_json)


@timeout(30)
def margin_detail_sse(date, as_json=False):
    """沪市融资融券明细"""
    df = ak.stock_margin_detail_sse(date=date)
    output(df, as_json=as_json, max_rows=30)


@timeout(30)
def margin_ratio(as_json=False):
    """两融余额占比"""
    df = ak.stock_margin_ratio_pa()
    output(df, as_json=as_json)


# ── IPO / 新股 ───────────────────────────────────────────────────────────────

@timeout(30)
def ipo_declare(as_json=False):
    """新股申购"""
    df = ak.stock_ipo_declare_em()
    output(df, as_json=as_json)


@timeout(30)
def ipo_list(as_json=False):
    """新股列表 (巨潮)"""
    df = ak.stock_new_ipo_cninfo()
    output(df, as_json=as_json, max_rows=30)


# ── Restricted Shares (限售解禁) ──────────────────────────────────────────────

@timeout(30)
def restricted_release(as_json=False):
    """限售解禁队列"""
    df = ak.stock_restricted_release_queue_em()
    output(df, as_json=as_json, max_rows=30)


# ── Stock Connect (沪深港通) ──────────────────────────────────────────────────

@timeout(30)
def hsgt_hist(symbol="沪股通", as_json=False):
    """沪深港通历史净买入"""
    df = ak.stock_hsgt_hist_em(symbol=symbol)
    output(df, as_json=as_json, max_rows=30)


@timeout(30)
def hsgt_fund_summary(as_json=False):
    """沪深港通资金汇总"""
    df = ak.stock_hsgt_fund_flow_summary_em()
    output(df, as_json=as_json)


# ── Valuation (估值) ─────────────────────────────────────────────────────────

@timeout(60)
def all_pb(as_json=False):
    """全 A 市净率"""
    info("Fetching all A PB ratio (~30s)...")
    df = ak.stock_a_all_pb()
    output(df, as_json=as_json, max_rows=30)


@timeout(60)
def all_pe(as_json=False):
    """全 A 市盈率"""
    info("Fetching all A PE ratio (~30s)...")
    df = ak.stock_a_ttm_lyr()
    output(df, as_json=as_json, max_rows=30)


# ── Research Reports & News ──────────────────────────────────────────────────

@timeout(15)
def research_report(as_json=False):
    """研报列表"""
    df = ak.stock_research_report_em()
    output(df, as_json=as_json, max_rows=30)


@timeout(15)
def stock_news(code, as_json=False):
    """个股新闻"""
    df = ak.stock_news_em(symbol=code)
    output(df, as_json=as_json)


@timeout(15)
def hot_rank(as_json=False):
    """热搜排名"""
    df = ak.stock_hot_rank_em()
    output(df, as_json=as_json, max_rows=30)


def main():
    parser = argparse.ArgumentParser(description="Special stock data")
    parser.add_argument("type", choices=[
        "lhb-detail", "lhb-stock", "lhb-stat",
        "zt-pool", "dt-pool", "zt-strong", "zt-previous",
        "margin-sse", "margin-szse", "margin-detail-sse", "margin-ratio",
        "ipo-declare", "ipo-list",
        "restricted-release",
        "hsgt-hist", "hsgt-summary",
        "all-pb", "all-pe",
        "research-report", "stock-news", "hot-rank"
    ])
    parser.add_argument("--code", help="Stock code")
    parser.add_argument("--date", help="Date YYYYMMDD")
    parser.add_argument("--start", help="Start date YYYYMMDD")
    parser.add_argument("--end", help="End date YYYYMMDD")
    parser.add_argument("--symbol", default="沪股通", help="For hsgt-hist")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    h = {
        "lhb-detail": lambda: lhb_detail(args.start, args.end, args.json),
        "lhb-stock": lambda: lhb_stock(args.code, args.json),
        "lhb-stat": lambda: lhb_stat(args.json),
        "zt-pool": lambda: zt_pool(args.date, args.json),
        "dt-pool": lambda: dt_pool(args.date, args.json),
        "zt-strong": lambda: zt_strong(args.date, args.json),
        "zt-previous": lambda: zt_previous(args.date, args.json),
        "margin-sse": lambda: margin_sse(args.start, args.end, args.json),
        "margin-szse": lambda: margin_szse(args.date, args.json),
        "margin-detail-sse": lambda: margin_detail_sse(args.date, args.json),
        "margin-ratio": lambda: margin_ratio(args.json),
        "ipo-declare": lambda: ipo_declare(args.json),
        "ipo-list": lambda: ipo_list(args.json),
        "restricted-release": lambda: restricted_release(args.json),
        "hsgt-hist": lambda: hsgt_hist(args.symbol, args.json),
        "hsgt-summary": lambda: hsgt_fund_summary(args.json),
        "all-pb": lambda: all_pb(args.json),
        "all-pe": lambda: all_pe(args.json),
        "research-report": lambda: research_report(args.json),
        "stock-news": lambda: stock_news(args.code, args.json),
        "hot-rank": lambda: hot_rank(args.json),
    }
    h[args.type]()


if __name__ == "__main__":
    main()
