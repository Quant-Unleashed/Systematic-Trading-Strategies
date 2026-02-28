import pandas as pd
from src.portfolio.turnover_control import TurnoverControl


class Backtester:

    def __init__(
        self,
        prices,
        strategy,
        transaction_cost=0.0005,
        rebalance="monthly"
    ):

        self.prices = prices
        self.strategy = strategy
        self.transaction_cost = transaction_cost
        self.rebalance = rebalance

        self.trade_log = None

    def calculate_turnover(self, weights):

        return weights.diff().abs().sum(axis=1)

    def generate_trade_log(self, weights):

        trades = weights.diff()

        trades = trades.stack().reset_index()

        trades.columns = ["date", "asset", "size"]

        self.trade_log = trades

    def apply_rebalance(self, weights):

        if self.rebalance == "daily":
            return weights

        if self.rebalance == "weekly":
            mask = weights.index.to_series().dt.weekday == 0

        elif self.rebalance == "monthly":
            mask = weights.index.to_series().dt.is_month_start

        else:
            raise ValueError("Unknown rebalance frequency")

        rebalance_weights = weights.where(mask)

        rebalance_weights = rebalance_weights.ffill()

        return rebalance_weights

    def run(self):

        weights = self.strategy.generate_weights(self.prices)

        weights = self.apply_rebalance(weights)

        turnover_model = TurnoverControl()

        weights = turnover_model.apply(weights)

        returns = self.prices.pct_change().fillna(0)

        portfolio_returns = (weights.shift(1) * returns).sum(axis=1)

        turnover = self.calculate_turnover(weights)

        costs = turnover * self.transaction_cost

        portfolio_returns = portfolio_returns - costs

        self.generate_trade_log(weights)

        return portfolio_returns
