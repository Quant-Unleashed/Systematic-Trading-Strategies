import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from run_backtests import run_strategy
from config.momentum_config import CONFIG

lookbacks = [21,63,126,252]
costs = [0.0001,0.0005,0.001]

results = []

for lb in lookbacks:
    for tc in costs:

        config = CONFIG.copy()

        config["momentum_lookback"] = [lb]
        config["transaction_cost"] = tc

        metrics = run_strategy(config)

        results.append((lb, tc, metrics["sharpe"]))

print("\nParameter Sweep Results")

for r in results:
    print(r)