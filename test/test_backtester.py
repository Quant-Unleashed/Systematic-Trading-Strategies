import pandas as pd
import numpy as np

from src.backtest.backtester import Backtester


def test_backtester_runs():

    prices = pd.DataFrame(
        np.random.rand(200, 3),
        columns=["A", "B", "C"]
    )

    class DummyStrategy:

        def generate_weights(self, prices):

            w = prices.copy()

            w[:] = 1 / len(prices.columns)

            return w

    bt = Backtester(prices, DummyStrategy())

    returns = bt.run()

    assert len(returns) == len(prices)