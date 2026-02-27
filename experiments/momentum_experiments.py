import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from run_backtests import run_strategy
from config.momentum_config import CONFIG as MOM


LOOKBACKS = {
    "1M": [21],
    "3M": [63],
    "12M": [252],
    "1M+3M": [21,63],
    "3M+12M": [63,252],
    "1M+3M+12M": [21,63,252]
}

results = []

for name, lb in LOOKBACKS.items():

    config = MOM.copy()
    config["momentum_lookback"] = lb

    metrics = run_strategy(config)

    results.append((name, metrics["sharpe"], metrics["oos_sharpe"]))

print("\nMomentum Experiments")

for r in results:
    print(r)
