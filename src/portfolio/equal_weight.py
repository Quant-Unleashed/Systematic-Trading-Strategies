class EqualWeightPortfolio:

    def construct(self, prices, signals):

        n_assets = signals.shape[1]

        weights = signals.copy()

        weights[:] = 1 / n_assets

        return weights
