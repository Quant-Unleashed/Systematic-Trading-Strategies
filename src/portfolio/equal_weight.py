class EqualWeightPortfolio:

    def allocate(self, signal):

        weights = signal.copy()

        weights = weights.div(weights.abs().sum(axis=1), axis=0)

        return weights