import pandas as pd


class Backtester:

    def __init__(
        self,
        prices,
        strategy,
        transaction_cost=0.0005,
        stop_loss=None
    ):

        self.prices = prices
        self.strategy = strategy
        self.transaction_cost = transaction_cost
        self.stop_loss = stop_loss

        self.trade_log = None

    def calculate_turnover(self, weights):

        return weights.diff().abs().sum(axis=1)

    def generate_trade_log(self, weights):

        trades = weights.diff()

        trades = trades.stack().reset_index()

        trades.columns = ["date", "asset", "size"]

        self.trade_log = trades

    def run(self):

        weights = self.strategy.generate_weights(self.prices)

        returns = self.prices.pct_change().fillna(0)

        portfolio_returns = (weights.shift(1) * returns).sum(axis=1)

        turnover = self.calculate_turnover(weights)

        costs = turnover * self.transaction_cost

        portfolio_returns = portfolio_returns - costs

        self.generate_trade_log(weights)

        return portfolio_returns