#!/usr/bin/env python3
"""
Special/thematic stock data: dragon list, limit up/down, margin, IPO, pledge,
goodwill, block trades, institutional research, stock connect, valuation, news.
Usage: python special.py <type> [--date DATE] [--code CODE] [--start START] [--end END] [--json]
"""
import sys, os
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _SCRIPT_DIR)
sys.path.insert(0, os.path.join(_SCRIPT_DIR, '..'))

import sys
import argparse
import akshare as ak
from common import output, error, info, timeout, validate_stock_code


# ══════════════════════════════════════════════════════════════════════════════
# 龙虎榜
# ══════════════════════════════════════════════════════════════════════════════

@timeout(30)
def lhb_detail(start, end, as_json=False):
    df = ak.stock_lhb_detail_em(start_date=start, end_date=end)
    output(df, as_json=as_json, max_rows=30)

@timeout(30)
def lhb_stock(code, as_json=False):
    df = ak.stock_lhb_stock_detail_em(symbol=code)
    output(df, as_json=as_json)

@timeout(30)
def lhb_stat(as_json=False):
    df = ak.stock_lhb_stock_statistic_em()
    output(df, as_json=as_json, max_rows=30)

@timeout(30)
def lhb_inst(as_json=False):
    """龙虎榜-机构统计"""
    df = ak.stock_lhb_jgstatistic_em()
    output(df, as_json=as_json, max_rows=30)

@timeout(30)
def lhb_trader(as_json=False):
    """龙虎榜-营业部统计"""
    df = ak.stock_lhb_traderstatistic_em()
    output(df, as_json=as_json, max_rows=30)

# ══════════════════════════════════════════════════════════════════════════════
# 涨跌停
# ══════════════════════════════════════════════════════════════════════════════

@timeout(30)
def zt_pool(date, as_json=False):
    df = ak.stock_zt_pool_em(date=date)
    output(df, as_json=as_json)

@timeout(30)
def dt_pool(date, as_json=False):
    df = ak.stock_zt_pool_dtgc_em(date=date)
    output(df, as_json=as_json)

@timeout(30)
def zt_strong(date, as_json=False):
    df = ak.stock_zt_pool_strong_em(date=date)
    output(df, as_json=as_json)

@timeout(30)
def zt_previous(date, as_json=False):
    df = ak.stock_zt_pool_previous_em(date=date)
    output(df, as_json=as_json)

@timeout(30)
def zt_sub_new(date, as_json=False):
    """次新股涨停"""
    df = ak.stock_zt_pool_sub_new_em(date=date)
    output(df, as_json=as_json)

@timeout(30)
def zt_zbgc(date, as_json=False):
    """涨停不打开"""
    df = ak.stock_zt_pool_zbgc_em(date=date)
    output(df, as_json=as_json)

# ══════════════════════════════════════════════════════════════════════════════
# 融资融券
# ══════════════════════════════════════════════════════════════════════════════

@timeout(30)
def margin_sse(start, end, as_json=False):
    df = ak.stock_margin_sse(start_date=start, end_date=end)
    output(df, as_json=as_json)

@timeout(30)
def margin_szse(date, as_json=False):
    df = ak.stock_margin_szse(date=date)
    output(df, as_json=as_json)

@timeout(30)
def margin_detail_sse(date, as_json=False):
    df = ak.stock_margin_detail_sse(date=date)
    output(df, as_json=as_json, max_rows=30)

@timeout(30)
def margin_ratio(as_json=False):
    df = ak.stock_margin_ratio_pa()
    output(df, as_json=as_json)

# ══════════════════════════════════════════════════════════════════════════════
# 股权质押
# ══════════════════════════════════════════════════════════════════════════════

@timeout(30)
def pledge_profile(as_json=False):
    """股权质押市场概况"""
    df = ak.stock_gpzy_profile_em()
    output(df, as_json=as_json)

@timeout(30)
def pledge_ratio(as_json=False):
    """上市公司质押比例"""
    df = ak.stock_gpzy_pledge_ratio_em()
    output(df, as_json=as_json, max_rows=30)

@timeout(30)
def pledge_detail(code, as_json=False):
    """重要股东股权质押明细"""
    df = ak.stock_gpzy_pledge_ratio_detail_em(symbol=code)
    output(df, as_json=as_json)

@timeout(30)
def pledge_bank(as_json=False):
    """质押机构分布-银行"""
    df = ak.stock_gpzy_distribute_statistics_bank_em()
    output(df, as_json=as_json)

@timeout(30)
def pledge_company(as_json=False):
    """质押机构分布-证券公司"""
    df = ak.stock_gpzy_distribute_statistics_company_em()
    output(df, as_json=as_json)

@timeout(30)
def pledge_industry(as_json=False):
    """质押行业数据"""
    df = ak.stock_gpzy_industry_data_em()
    output(df, as_json=as_json)

# ══════════════════════════════════════════════════════════════════════════════
# 商誉
# ══════════════════════════════════════════════════════════════════════════════

@timeout(30)
def goodwill_profile(as_json=False):
    """A股商誉市场概况"""
    df = ak.stock_sy_profile_em()
    output(df, as_json=as_json)

@timeout(30)
def goodwill_expected(as_json=False):
    """商誉减值预期明细"""
    df = ak.stock_sy_yq_em()
    output(df, as_json=as_json, max_rows=30)

@timeout(30)
def goodwill_detail(code, as_json=False):
    """个股商誉减值明细"""
    df = ak.stock_sy_jz_em(symbol=code)
    output(df, as_json=as_json)

@timeout(30)
def goodwill_stock(code, as_json=False):
    """个股商誉明细"""
    df = ak.stock_sy_em(symbol=code)
    output(df, as_json=as_json)

@timeout(30)
def goodwill_industry(as_json=False):
    """行业商誉"""
    df = ak.stock_sy_hy_em()
    output(df, as_json=as_json)

# ══════════════════════════════════════════════════════════════════════════════
# 机构调研
# ══════════════════════════════════════════════════════════════════════════════

@timeout(30)
def inst_research_stat(as_json=False):
    """机构调研-统计"""
    df = ak.stock_jgdy_tj_em()
    output(df, as_json=as_json, max_rows=30)

@timeout(30)
def inst_research_detail(code, as_json=False):
    """机构调研-详细"""
    df = ak.stock_jgdy_detail_em(symbol=code)
    output(df, as_json=as_json)

@timeout(30)
def analyst_rank(as_json=False):
    """分析师排名"""
    df = ak.stock_analyst_rank_em()
    output(df, as_json=as_json, max_rows=30)

@timeout(30)
def inst_recommend(as_json=False):
    """机构推荐"""
    df = ak.stock_institute_recommend()
    output(df, as_json=as_json, max_rows=30)

# ══════════════════════════════════════════════════════════════════════════════
# 大宗交易
# ══════════════════════════════════════════════════════════════════════════════

@timeout(30)
def block_trade_daily(date, as_json=False):
    """大宗交易每日统计"""
    df = ak.stock_dzjy_mrtj(date=date)
    output(df, as_json=as_json)

@timeout(30)
def block_trade_detail(date, as_json=False):
    """大宗交易每日明细"""
    df = ak.stock_dzjy_mrmx(date=date)
    output(df, as_json=as_json, max_rows=30)

@timeout(30)
def block_trade_sector(date, as_json=False):
    """大宗交易-行业成交统计"""
    df = ak.stock_dzjy_hygtj(date=date)
    output(df, as_json=as_json)

@timeout(30)
def block_trade_sector_rank(date, as_json=False):
    """大宗交易-营业部排行"""
    df = ak.stock_dzjy_yybph(date=date)
    output(df, as_json=as_json, max_rows=30)

# ══════════════════════════════════════════════════════════════════════════════
# IPO / 新股
# ══════════════════════════════════════════════════════════════════════════════

@timeout(30)
def ipo_declare(as_json=False):
    df = ak.stock_ipo_declare_em()
    output(df, as_json=as_json)

@timeout(30)
def ipo_list(as_json=False):
    df = ak.stock_new_ipo_cninfo()
    output(df, as_json=as_json, max_rows=30)

# ══════════════════════════════════════════════════════════════════════════════
# 限售解禁
# ══════════════════════════════════════════════════════════════════════════════

@timeout(30)
def restricted_release(as_json=False):
    df = ak.stock_restricted_release_queue_em()
    output(df, as_json=as_json, max_rows=30)

@timeout(30)
def restricted_summary(as_json=False):
    """限售解禁汇总"""
    df = ak.stock_restricted_release_summary_em()
    output(df, as_json=as_json)

@timeout(30)
def restricted_detail(code, as_json=False):
    """个股限售解禁详情"""
    df = ak.stock_restricted_release_detail_em(symbol=code)
    output(df, as_json=as_json)

# ══════════════════════════════════════════════════════════════════════════════
# 沪深港通
# ══════════════════════════════════════════════════════════════════════════════

@timeout(30)
def hsgt_hist(symbol="沪股通", as_json=False):
    df = ak.stock_hsgt_hist_em(symbol=symbol)
    output(df, as_json=as_json, max_rows=30)

@timeout(30)
def hsgt_fund_summary(as_json=False):
    df = ak.stock_hsgt_fund_flow_summary_em()
    output(df, as_json=as_json)

@timeout(30)
def hsgt_hold(as_json=False):
    """沪深港通持股"""
    df = ak.stock_hsgt_hold_stock_em(market="北向", indicator="今日排行")
    output(df, as_json=as_json, max_rows=30)

@timeout(30)
def hsgt_board_rank(as_json=False):
    """沪深港通板块排名"""
    df = ak.stock_hsgt_board_rank_em(symbol="北向资金增持行业板块排行", indicator="今日")
    output(df, as_json=as_json, max_rows=30)

# ══════════════════════════════════════════════════════════════════════════════
# 估值
# ══════════════════════════════════════════════════════════════════════════════

@timeout(60)
def all_pb(as_json=False):
    info("Fetching all A PB ratio (~30s)...")
    df = ak.stock_a_all_pb()
    output(df, as_json=as_json, max_rows=30)

@timeout(60)
def all_pe(as_json=False):
    info("Fetching all A PE ratio (~30s)...")
    df = ak.stock_a_ttm_lyr()
    output(df, as_json=as_json, max_rows=30)

@timeout(15)
def stock_valuation(code, as_json=False):
    """个股估值对比"""
    df = ak.stock_zh_valuation_comparison_em(symbol=code)
    output(df, as_json=as_json)

# ══════════════════════════════════════════════════════════════════════════════
# 研报 & 新闻 & 热度
# ══════════════════════════════════════════════════════════════════════════════

@timeout(15)
def research_report(as_json=False):
    df = ak.stock_research_report_em()
    output(df, as_json=as_json, max_rows=30)

@timeout(15)
def stock_news(code, as_json=False):
    df = ak.stock_news_em(symbol=code)
    output(df, as_json=as_json)

@timeout(15)
def hot_rank(as_json=False):
    df = ak.stock_hot_rank_em()
    output(df, as_json=as_json, max_rows=30)

@timeout(15)
def hot_keyword(as_json=False):
    """热门关键词"""
    df = ak.stock_hot_keyword_em()
    output(df, as_json=as_json, max_rows=30)

@timeout(15)
def stock_comment(code, as_json=False):
    """股吧评论"""
    df = ak.stock_comment_em(symbol=code)
    output(df, as_json=as_json, max_rows=30)

# ══════════════════════════════════════════════════════════════════════════════
# 公告 & 股东变化
# ══════════════════════════════════════════════════════════════════════════════

@timeout(30)
def notice_report(code, as_json=False):
    """个股公告"""
    df = ak.stock_notice_report(symbol=code, indicator="全部")
    output(df, as_json=as_json, max_rows=30)

@timeout(30)
def shareholder_change(code, as_json=False):
    """股东变化（同花顺）"""
    df = ak.stock_shareholder_change_ths(symbol=code)
    output(df, as_json=as_json)

@timeout(30)
def company_changes(code, as_json=False):
    """公司变动"""
    df = ak.stock_changes_em(symbol=code)
    output(df, as_json=as_json)

@timeout(30)
def stock_repurchase(code, as_json=False):
    """股票回购"""
    df = ak.stock_repurchase_em(symbol=code)
    output(df, as_json=as_json)

@timeout(30)
def revenue_timing(code, as_json=False):
    """营收数据"""
    df = ak.stock_yysj_em(symbol=code)
    output(df, as_json=as_json)

# ══════════════════════════════════════════════════════════════════════════════
# 资金流-大单
# ══════════════════════════════════════════════════════════════════════════════

@timeout(30)
def fund_flow_big(as_json=False):
    """大单资金流向"""
    df = ak.stock_fund_flow_big_deal()
    output(df, as_json=as_json, max_rows=30)

# ══════════════════════════════════════════════════════════════════════════════
# 可转债
# ══════════════════════════════════════════════════════════════════════════════

@timeout(30)
def convert_bond_jsl(as_json=False):
    """可转债实时数据（集思录）"""
    df = ak.bond_cb_jsl()
    output(df, as_json=as_json, max_rows=30)

@timeout(30)
def convert_bond_redeem(as_json=False):
    """可转债强赎（集思录）"""
    df = ak.bond_cb_redeem_jsl()
    output(df, as_json=as_json, max_rows=30)

@timeout(30)
def convert_bond_index(as_json=False):
    """集思录可转债等权指数"""
    df = ak.bond_cb_index_jsl()
    output(df, as_json=as_json, max_rows=30)

@timeout(30)
def convert_bond_adj(as_json=False):
    """可转债转股价变动"""
    df = ak.bond_cb_adj_logs_jsl()
    output(df, as_json=as_json, max_rows=30)


def main():
    parser = argparse.ArgumentParser(description="Special/thematic stock data")
    parser.add_argument("type", choices=[
        # 龙虎榜
        "lhb-detail", "lhb-stock", "lhb-stat", "lhb-inst", "lhb-trader",
        # 涨跌停
        "zt-pool", "dt-pool", "zt-strong", "zt-previous", "zt-sub-new", "zt-zbgc",
        # 融资融券
        "margin-sse", "margin-szse", "margin-detail-sse", "margin-ratio",
        # 股权质押
        "pledge-profile", "pledge-ratio", "pledge-detail", "pledge-bank",
        "pledge-company", "pledge-industry",
        # 商誉
        "goodwill-profile", "goodwill-expected", "goodwill-detail",
        "goodwill-stock", "goodwill-industry",
        # 机构调研
        "inst-research-stat", "inst-research-detail", "analyst-rank", "inst-recommend",
        # 大宗交易
        "block-daily", "block-detail", "block-sector", "block-sector-rank",
        # IPO
        "ipo-declare", "ipo-list",
        # 限售解禁
        "restricted-release", "restricted-summary", "restricted-detail",
        # 沪深港通
        "hsgt-hist", "hsgt-summary", "hsgt-hold", "hsgt-board-rank",
        # 估值
        "all-pb", "all-pe", "stock-valuation",
        # 研报/新闻/热度
        "research-report", "stock-news", "hot-rank", "hot-keyword", "stock-comment",
        # 公告/股东/变动
        "notice-report", "shareholder-change", "company-changes", "stock-repurchase",
        "revenue-timing",
        # 大单资金
        "fund-flow-big",
        # 可转债
        "convert-bond-jsl", "convert-bond-redeem", "convert-bond-index", "convert-bond-adj",
    ])
    parser.add_argument("--code", help="Stock code")
    parser.add_argument("--date", help="Date YYYYMMDD")
    parser.add_argument("--start", help="Start date YYYYMMDD")
    parser.add_argument("--end", help="End date YYYYMMDD")
    parser.add_argument("--symbol", default="沪股通", help="For hsgt-hist")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.code:
        validate_stock_code(args.code)

    j = args.json
    h = {
        # 龙虎榜
        "lhb-detail": lambda: lhb_detail(args.start, args.end, j),
        "lhb-stock": lambda: lhb_stock(args.code, j),
        "lhb-stat": lambda: lhb_stat(j),
        "lhb-inst": lambda: lhb_inst(j),
        "lhb-trader": lambda: lhb_trader(j),
        # 涨跌停
        "zt-pool": lambda: zt_pool(args.date, j),
        "dt-pool": lambda: dt_pool(args.date, j),
        "zt-strong": lambda: zt_strong(args.date, j),
        "zt-previous": lambda: zt_previous(args.date, j),
        "zt-sub-new": lambda: zt_sub_new(args.date, j),
        "zt-zbgc": lambda: zt_zbgc(args.date, j),
        # 融资融券
        "margin-sse": lambda: margin_sse(args.start, args.end, j),
        "margin-szse": lambda: margin_szse(args.date, j),
        "margin-detail-sse": lambda: margin_detail_sse(args.date, j),
        "margin-ratio": lambda: margin_ratio(j),
        # 股权质押
        "pledge-profile": lambda: pledge_profile(j),
        "pledge-ratio": lambda: pledge_ratio(j),
        "pledge-detail": lambda: pledge_detail(args.code, j),
        "pledge-bank": lambda: pledge_bank(j),
        "pledge-company": lambda: pledge_company(j),
        "pledge-industry": lambda: pledge_industry(j),
        # 商誉
        "goodwill-profile": lambda: goodwill_profile(j),
        "goodwill-expected": lambda: goodwill_expected(j),
        "goodwill-detail": lambda: goodwill_detail(args.code, j),
        "goodwill-stock": lambda: goodwill_stock(args.code, j),
        "goodwill-industry": lambda: goodwill_industry(j),
        # 机构调研
        "inst-research-stat": lambda: inst_research_stat(j),
        "inst-research-detail": lambda: inst_research_detail(args.code, j),
        "analyst-rank": lambda: analyst_rank(j),
        "inst-recommend": lambda: inst_recommend(j),
        # 大宗交易
        "block-daily": lambda: block_trade_daily(args.date, j),
        "block-detail": lambda: block_trade_detail(args.date, j),
        "block-sector": lambda: block_trade_sector(args.date, j),
        "block-sector-rank": lambda: block_trade_sector_rank(args.date, j),
        # IPO
        "ipo-declare": lambda: ipo_declare(j),
        "ipo-list": lambda: ipo_list(j),
        # 限售解禁
        "restricted-release": lambda: restricted_release(j),
        "restricted-summary": lambda: restricted_summary(j),
        "restricted-detail": lambda: restricted_detail(args.code, j),
        # 沪深港通
        "hsgt-hist": lambda: hsgt_hist(args.symbol, j),
        "hsgt-summary": lambda: hsgt_fund_summary(j),
        "hsgt-hold": lambda: hsgt_hold(j),
        "hsgt-board-rank": lambda: hsgt_board_rank(j),
        # 估值
        "all-pb": lambda: all_pb(j),
        "all-pe": lambda: all_pe(j),
        "stock-valuation": lambda: stock_valuation(args.code, j),
        # 研报/新闻/热度
        "research-report": lambda: research_report(j),
        "stock-news": lambda: stock_news(args.code, j),
        "hot-rank": lambda: hot_rank(j),
        "hot-keyword": lambda: hot_keyword(j),
        "stock-comment": lambda: stock_comment(args.code, j),
        # 公告/股东/变动
        "notice-report": lambda: notice_report(args.code, j),
        "shareholder-change": lambda: shareholder_change(args.code, j),
        "company-changes": lambda: company_changes(args.code, j),
        "stock-repurchase": lambda: stock_repurchase(args.code, j),
        "revenue-timing": lambda: revenue_timing(args.code, j),
        # 大单
        "fund-flow-big": lambda: fund_flow_big(j),
        # 可转债
        "convert-bond-jsl": lambda: convert_bond_jsl(j),
        "convert-bond-redeem": lambda: convert_bond_redeem(j),
        "convert-bond-index": lambda: convert_bond_index(j),
        "convert-bond-adj": lambda: convert_bond_adj(j),
    }
    h[args.type]()


if __name__ == "__main__":
    main()
