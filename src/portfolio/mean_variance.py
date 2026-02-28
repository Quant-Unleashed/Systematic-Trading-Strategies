import numpy as np
import pandas as pd

class MeanVariance:

    def construct(self, prices, signals):

        returns = prices.pct_change().dropna()

        cov = returns.cov()

        inv_cov = np.linalg.pinv(cov.values)

        raw_weights = inv_cov.sum(axis=1)

        weights = raw_weights / raw_weights.sum()

        weights = pd.Series(weights, index=prices.columns)

        return pd.DataFrame([weights]*len(prices), index=prices.index)
