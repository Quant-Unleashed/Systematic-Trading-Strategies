import numpy as np


class VolatilityScaler:

    def __init__(self, lookback=20, target_vol=0.10):
        self.lookback = lookback
        self.target_vol = target_vol

    def apply(self, prices, weights):

        returns = prices.pct_change()

        vol = returns.rolling(self.lookback).std() * np.sqrt(252)

        scaling = self.target_vol / vol

        scaled = weights * scaling

        # normalize portfolio exposure
        scaled = scaled.div(scaled.abs().sum(axis=1), axis=0)

        return scaled