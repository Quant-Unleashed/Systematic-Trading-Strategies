import pandas as pd
import numpy as np

from src.portfolio.equal_weight import EqualWeightPortfolio


def test_equal_weight():

    dates = pd.date_range("2020-01-01", periods=50)

    signals = pd.DataFrame(
        np.random.rand(50,4),
        index=dates,
        columns=list("ABCD")
    )

    portfolio = EqualWeightPortfolio()

    weights = portfolio.construct(None, signals)

    assert abs(weights.sum(axis=1).iloc[0] - 1) < 1e-6
