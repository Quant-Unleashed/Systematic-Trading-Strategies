import pandas as pd
from .base_signal import BaseSignal


class MomentumSignal(BaseSignal):

    def __init__(self, lookbacks=[21, 63, 252]):

        # Allow int or list
        if isinstance(lookbacks, int):
            lookbacks = [lookbacks]

        self.lookbacks = lookbacks

    def generate(self, prices):

        signals = []

        for lb in self.lookbacks:

            mom = prices.pct_change(lb)

            signals.append(mom)

        combined = sum(signals) / len(signals)

        weights = combined.rank(axis=1, pct=True)

        weights = weights.sub(weights.mean(axis=1), axis=0)

        return weights
