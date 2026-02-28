import itertools

from config.research_config import RESEARCH_CONFIG
from config.base_config import BASE_CONFIG


def generate_strategies():

    configs = []

    momentum_lookbacks = RESEARCH_CONFIG["momentum_lookbacks"]
    vol_targets = RESEARCH_CONFIG["vol_targets"]
    regimes = RESEARCH_CONFIG["regime_filters"]
    portfolio_models = RESEARCH_CONFIG["portfolio_models"]

    for lookback, vol, regime, portfolio in itertools.product(
        momentum_lookbacks,
        vol_targets,
        regimes,
        portfolio_models
    ):

        strategy_name = "momentum"

        if vol:
            strategy_name += "_vol"

        if regime:
            strategy_name += "_regime"

        config = {

            **BASE_CONFIG,

            "strategy": strategy_name,

            "momentum_lookback": lookback,

            "vol_target": vol,

            "regime_filter": regime,

            "portfolio_model": portfolio

        }

        configs.append(config)

    return configs
