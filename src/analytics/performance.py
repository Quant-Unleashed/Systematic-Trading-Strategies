import numpy as np
import pandas as pd

TRADING_DAYS = 252


class Performance:

    @staticmethod
    def total_return(returns):
        return (1 + returns).prod() - 1

    @staticmethod
    def annual_return(returns):
        return returns.mean() * 252

    @staticmethod
    def volatility(returns):
        return returns.std() * np.sqrt(TRADING_DAYS)

    @staticmethod
    def sharpe(returns):
        return np.sqrt(TRADING_DAYS) * returns.mean() / returns.std()

    @staticmethod
    def sortino(returns):
        downside = returns[returns < 0]
        downside_std = downside.std() * np.sqrt(TRADING_DAYS)
        return returns.mean() * TRADING_DAYS / downside_std

    @staticmethod
    def max_drawdown(equity):
        running_max = equity.cummax()
        drawdown = equity / running_max - 1
        return drawdown.min()

    @staticmethod
    def calmar(returns):
        equity = (1 + returns).cumprod()
        annual_return = Performance.annual_return(returns)
        mdd = abs(Performance.max_drawdown(equity))
        return annual_return / mdd if mdd != 0 else np.nan

    @staticmethod
    def win_rate(returns):
        return (returns > 0).mean()

    @staticmethod
    def rolling_sharpe(returns, window=252):
        return returns.rolling(window).mean() / returns.rolling(window).std() * np.sqrt(252)

    @staticmethod
    def rolling_drawdown(equity):
        running_max = equity.cummax()
        return equity / running_max - 1

    @staticmethod
    def turnover(weights):
        return weights.diff().abs().sum(axis=1).mean()

    @staticmethod
    def profit_factor(returns):
        wins = returns[returns > 0].sum()
        losses = abs(returns[returns < 0].sum())
        return wins / losses
