import numpy as np


class VolTarget:

    def __init__(self, target_vol=0.10):
        self.target_vol = target_vol

    def apply(self, weights, returns):

        vol = returns.rolling(20).std() * np.sqrt(252)

        scaling = self.target_vol / vol

        adjusted = weights * scaling

        return adjusted