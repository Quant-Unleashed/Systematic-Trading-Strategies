class Strategy:

    def __init__(self, signal_pipeline, portfolio):

        self.signal_pipeline = signal_pipeline
        self.portfolio = portfolio


    def generate_weights(self, prices):

        signal = self.signal_pipeline.generate(prices)

        weights = self.portfolio.construct(prices, signal)

        return weights