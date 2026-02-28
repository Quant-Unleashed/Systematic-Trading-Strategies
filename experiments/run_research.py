import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
from pathlib import Path

from experiments.strategy_generator import generate_strategies
from run_backtests import run_strategy


def main():

    print("\n========== STRATEGY RESEARCH ==========\n")

    configs = generate_strategies()

    total = len(configs)

    print(f"Total strategies to evaluate: {total}\n")

    results = []

    for i, config in enumerate(configs):

        print(f"Running strategy {i+1}/{total}")

        metrics = run_strategy(config)

        results.append({

            "strategy": config.get("strategy"),
            "lookbacks": config.get("momentum_lookback"),
            "portfolio": config.get("portfolio_model"),

            "annual_return": metrics.get("annual_return"),
            "sharpe": metrics.get("sharpe"),
            "oos_sharpe": metrics.get("oos_sharpe"),
            "max_drawdown": metrics.get("max_drawdown")
        })

    df = pd.DataFrame(results)

    df = df.sort_values("sharpe", ascending=False)

    Path("reports").mkdir(exist_ok=True)

    output_file = "reports/research_leaderboard.csv"

    df.to_csv(output_file, index=False)

    print("\n========== RESEARCH COMPLETE ==========\n")

    print(f"Results saved to: {output_file}\n")

    print("Top Strategies:")

    print(df.head(10))


if __name__ == "__main__":

    main()
