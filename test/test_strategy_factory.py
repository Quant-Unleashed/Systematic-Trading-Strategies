from src.strategies.strategy_factory import StrategyFactory


def test_strategy_factory():

    config = {
        "strategy": "momentum",
        "momentum_lookback": [21]
    }

    strategy = StrategyFactory.build(config)

    assert strategy is not None
