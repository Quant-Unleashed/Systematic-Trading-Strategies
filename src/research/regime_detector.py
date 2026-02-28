import pandas as pd


class RegimeDetector:

    def __init__(self, lookback=200):

        self.lookback = lookback

    def detect(self, prices):

        ma = prices.rolling(self.lookback).mean()

        regime = prices > ma

        regime = regime.astype(int)

        return regime
