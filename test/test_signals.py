import pandas as pd
import numpy as np

from src.signals.momentum_signal import MomentumSignal


def test_momentum_signal():

    dates = pd.date_range("2020-01-01", periods=200)

    prices = pd.DataFrame(
        np.random.rand(200,3),
        index=dates,
        columns=["A","B","C"]
    )

    signal = MomentumSignal([21,63])

    weights = signal.generate(prices)

    assert weights.shape == prices.shape
