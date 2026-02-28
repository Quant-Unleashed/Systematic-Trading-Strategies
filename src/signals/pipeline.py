class SignalPipeline:

    def __init__(self, signal, transforms=None):

        self.signal = signal
        self.transforms = transforms if transforms else []

    def generate(self, prices):

        weights = self.signal.generate(prices)

        for t in self.transforms:

            weights = t.apply(prices, weights)

        return weights
