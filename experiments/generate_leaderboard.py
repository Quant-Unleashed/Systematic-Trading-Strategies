import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
from pathlib import Path

from run_backtests import run_strategy

from config.momentum_config import CONFIG as MOM
from config.momentum_vol_config import CONFIG as MOM_VOL
from config.momentum_vol_regime_config import CONFIG as MOM_FULL


STRATEGIES = {
    "Momentum": MOM,
    "Momentum + Vol Target": MOM_VOL,
    "Momentum + Vol + Regime": MOM_FULL
}

results = []

for name, config in STRATEGIES.items():

    metrics = run_strategy(config)

    results.append({
        "Strategy": name,
        "Annual Return": metrics["annual_return"],
        "Sharpe": metrics["sharpe"],
        "OOS Sharpe": metrics["oos_sharpe"],
        "Max Drawdown": metrics["max_drawdown"]
    })


df = pd.DataFrame(results)

df = df.sort_values("Sharpe", ascending=False)

Path("reports").mkdir(exist_ok=True)

df.to_csv("reports/strategy_leaderboard.csv", index=False)

print("\nLeaderboard\n")
print(df)
