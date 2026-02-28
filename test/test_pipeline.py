import pandas as pd
import numpy as np

from src.signals.pipeline import SignalPipeline


class DummySignal:

    def generate(self, prices):

        return pd.DataFrame(
            1,
            index=prices.index,
            columns=prices.columns
        )


def test_pipeline():

    dates = pd.date_range("2020-01-01", periods=20)

    prices = pd.DataFrame(
        np.random.rand(20,3),
        index=dates,
        columns=["A","B","C"]
    )

    pipeline = SignalPipeline(DummySignal())

    weights = pipeline.generate(prices)

    assert weights.shape == prices.shape
