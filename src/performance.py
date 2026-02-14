import numpy as np
import pandas as pd


TRADING_DAYS = 252


def calculate_cagr(returns):
    cumulative = (1 + returns).prod()
    years = len(returns) / TRADING_DAYS
    return cumulative ** (1 / years) - 1


def calculate_sharpe(returns):
    return np.sqrt(TRADING_DAYS) * returns.mean() / returns.std()


def calculate_max_drawdown(equity_curve):
    running_max = equity_curve.cummax()
    drawdown = equity_curve / running_max - 1
    return drawdown.min(), drawdown


def performance_summary(returns):
    equity_curve = (1 + returns).cumprod()

    cagr = calculate_cagr(returns)
    sharpe = calculate_sharpe(returns)
    max_dd, drawdown_series = calculate_max_drawdown(equity_curve)
    vol = returns.std() * np.sqrt(TRADING_DAYS)

    summary = {
        "CAGR": cagr,
        "Sharpe": sharpe,
        "Max Drawdown": max_dd,
        "Volatility": vol,
    }

    return summary, equity_curve, drawdown_series
