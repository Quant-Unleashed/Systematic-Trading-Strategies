import numpy as np

class InverseVolatility:

    def construct(self, prices, signals):

        returns = prices.pct_change()

        vol = returns.rolling(60).std()

        inv_vol = 1 / vol

        weights = signals * inv_vol

        weights = weights.div(weights.abs().sum(axis=1), axis=0)

        return weights
