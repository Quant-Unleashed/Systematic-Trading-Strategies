import pandas as pd
import numpy as np

from src.backtest.backtester import Backtester


class DummyStrategy:

    def generate_weights(self, prices):

        return pd.DataFrame(
            1 / prices.shape[1],
            index=prices.index,
            columns=prices.columns
        )


def test_backtester_runs():

    dates = pd.date_range("2020-01-01", periods=100)

    prices = pd.DataFrame(
        np.random.rand(100,3),
        index=dates,
        columns=["A","B","C"]
    )

    bt = Backtester(prices, DummyStrategy())

    returns = bt.run()

    assert len(returns) == len(prices)
