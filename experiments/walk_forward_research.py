import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pandas as pd

from src.research.walk_forward import WalkForwardOptimizer
from src.data.data_loader import DataLoader

from config.base_config import BASE_CONFIG
from experiments.strategy_generator import generate_strategies
from run_backtests import run_strategy


def backtest_subset(prices, config):

    metrics = run_strategy(config)

    return metrics


configs = generate_strategies()

optimizer = WalkForwardOptimizer()

loader = DataLoader(
    BASE_CONFIG["tickers"],
    BASE_CONFIG["start_date"],
    BASE_CONFIG["end_date"]
)

prices = loader.load()

returns = optimizer.run(prices, configs, backtest_subset)

equity = (1 + returns).cumprod()

equity.to_csv("reports/walk_forward_equity.csv")

print("Walk-forward completed")
