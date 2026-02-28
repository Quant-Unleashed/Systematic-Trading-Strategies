from src.portfolio.equal_weight import EqualWeightPortfolio
from src.portfolio.inverse_vol import InverseVolatility
from src.portfolio.mean_variance import MeanVariance


class PortfolioFactory:

    @staticmethod
    def build(name):

        if name == "equal_weight":
            return EqualWeightPortfolio()

        if name == "inverse_vol":
            return InverseVolatility()

        if name == "mean_variance":
            return MeanVariance()

        raise ValueError("Unknown portfolio model")
