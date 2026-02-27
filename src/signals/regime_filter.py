class RegimeFilter:

    def __init__(self, lookback=200):
        self.lookback = lookback

    def apply(self, prices, weights):

        ma = prices.rolling(self.lookback).mean()

        regime = prices > ma

        return weights * regime