class TurnoverControl:

    def __init__(self, max_turnover=0.25):
        self.max_turnover = max_turnover

    def apply(self, weights):

        prev = weights.shift(1)

        turnover = (weights - prev).abs()

        capped = prev + turnover.clip(upper=self.max_turnover) * (weights - prev).apply(lambda x: x/x.abs())

        capped = capped.fillna(weights)

        return capped
