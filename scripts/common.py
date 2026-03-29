#!/usr/bin/env python3
"""
akshare-open common utilities.
Shared helpers for timeout, retry, output formatting, and error handling.
"""

import sys
import json
import time
import signal
import functools
from typing import Any, Optional

import pandas as pd


# ── Timeout ──────────────────────────────────────────────────────────────────

class TimeoutError(Exception):
    pass


def timeout(seconds: int = 30):
    """Decorator: kill function if it exceeds `seconds`."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            def handler(signum, frame):
                raise TimeoutError(f"Operation timed out after {seconds}s")
            old = signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)
            try:
                return func(*args, **kwargs)
            finally:
                signal.alarm(0)
                signal.signal(signal.SIGALRM, old)
        return wrapper
    return decorator


# ── Retry ────────────────────────────────────────────────────────────────────

def retry(max_attempts: int = 3, delay: float = 2.0):
    """Decorator: retry on exception up to max_attempts."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    if attempt < max_attempts:
                        print(f"  ⚠ Attempt {attempt}/{max_attempts} failed: {e}, retrying in {delay}s...", file=sys.stderr)
                        time.sleep(delay)
            raise last_exc
        return wrapper
    return decorator


# ── Output ───────────────────────────────────────────────────────────────────

def output(df: pd.DataFrame, as_json: bool = False, max_rows: int = 50):
    """Print DataFrame as JSON or pretty table."""
    if df is None or df.empty:
        print("No data returned.")
        return

    if as_json:
        records = df.to_dict(orient="records")
        print(json.dumps(records, ensure_ascii=False, indent=2, default=str))
    else:
        # Pretty print with tabulate-like formatting
        display = df.head(max_rows) if len(df) > max_rows else df
        print(display.to_string(index=False))
        if len(df) > max_rows:
            print(f"\n... ({len(df)} total rows, showing first {max_rows})")


def output_dict(data: dict, as_json: bool = False):
    """Print a dict as JSON or key-value pairs."""
    if as_json:
        print(json.dumps(data, ensure_ascii=False, indent=2, default=str))
    else:
        for k, v in data.items():
            print(f"{k}: {v}")


def error(msg: str):
    """Print error to stderr and exit."""
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def info(msg: str):
    """Print info to stderr (not polluting stdout for JSON piping)."""
    print(f"  ℹ {msg}", file=sys.stderr)


# ── Date helpers ─────────────────────────────────────────────────────────────

def today_str() -> str:
    """Return today as YYYYMMDD."""
    from datetime import datetime
    return datetime.now().strftime("%Y%m%d")


def recent_trade_date(days_back: int = 3) -> str:
    """Return a recent date likely to be a trading day."""
    from datetime import datetime, timedelta
    d = datetime.now()
    # Go back enough to likely hit a trading day
    while d.weekday() >= 5:  # skip weekends
        d -= timedelta(days=1)
    return d.strftime("%Y%m%d")


# ── Safe access ──────────────────────────────────────────────────────────────

def safe_float(val) -> Optional[float]:
    """Convert to float, return None on failure."""
    try:
        f = float(val)
        return f if f == f else None  # NaN check
    except (TypeError, ValueError):
        return None


# ── Stock code validation ────────────────────────────────────────────────────

import re

def validate_stock_code(code: str, market: str = "auto") -> bool:
    """
    Validate stock code format.
    Returns True if valid, calls error() on failure.

    Supported formats:
      - A股: 6 digits (6xxxxx沪, 0xxxxx深, 3xxxxx创业板, 688xxx科创板, 8/4xxxxx北证)
      - 港股: 5 digits (e.g., 00700)
      - 美股: 1-5 uppercase letters (e.g., AAPL)
      - 指数: sh000001 / sz399001 等前缀格式，或纯数字
    """
    if not code:
        error("股票代码不能为空")

    code = code.strip()

    # US stock: letters only
    if re.match(r'^[A-Z]{1,5}$', code):
        return True

    # Index with prefix: sh000001, sz399001
    if re.match(r'^(sh|sz|bj)\d{6}$', code):
        return True

    # Pure digits
    if re.match(r'^\d+$', code):
        # A股: 6 digits
        if len(code) == 6:
            return True
        # 港股: 5 digits
        if len(code) == 5:
            return True
        # 其他长度数字
        error(f"股票代码格式错误: '{code}'（A股/指数需6位，港股需5位）")

    error(f"股票代码格式错误: '{code}'（A股: 6位数字，港股: 5位数字，美股: 大写字母）")


def format_number(n, unit: str = "") -> str:
    """Format large numbers with 万/亿."""
    if n is None:
        return "N/A"
    n = float(n)
    if abs(n) >= 1e8:
        return f"{n/1e8:.2f}亿{unit}"
    elif abs(n) >= 1e4:
        return f"{n/1e4:.2f}万{unit}"
    else:
        return f"{n:.2f}{unit}"
