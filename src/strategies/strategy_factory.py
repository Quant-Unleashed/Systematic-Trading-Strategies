from src.signals.momentum_signal import MomentumSignal
from src.signals.vol_target import VolTarget
from src.signals.regime_filter import RegimeFilter
from src.signals.pipeline import SignalPipeline

from src.portfolio.equal_weight import EqualWeightPortfolio
from src.portfolio.portfolio_factory import PortfolioFactory

from src.strategies.momentum_strategy import Strategy


class StrategyFactory:

    @staticmethod
    def build(CONFIG):

        strategy_name = CONFIG["strategy"]

        signal = MomentumSignal(CONFIG["momentum_lookback"])

        transforms = []

        if CONFIG.get("vol_target"):

            transforms.append(VolTarget(CONFIG["vol_target"]))

        if CONFIG.get("regime_filter"):

            transforms.append(RegimeFilter())

        pipeline = SignalPipeline(signal, transforms)

        portfolio_model = CONFIG.get("portfolio_model", "equal_weight")

        portfolio = PortfolioFactory.build(portfolio_model)

        return Strategy(pipeline, portfolio)

