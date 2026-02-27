class Strategy:

    def __init__(self, signal_pipeline, portfolio_model):

        self.signal_pipeline = signal_pipeline
        self.portfolio_model = portfolio_model

    def generate_weights(self, prices):

        signal = self.signal_pipeline.generate(prices)

        weights = self.portfolio_model.allocate(signal)

        return weights