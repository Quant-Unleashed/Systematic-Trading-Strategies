import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

FIGURES_PATH = Path("reports/figures")
FIGURES_PATH.mkdir(parents=True, exist_ok=True)


def plot_equity_curve(equity_curve, oos_date):
    plt.figure(figsize=(12,6))
    equity_curve.plot(label="Portfolio")

    # Out-of-sample vertical line
    plt.axvline(pd.to_datetime(oos_date), linestyle="--", linewidth=2, label="OOS start")

    plt.title("Portfolio Equity Curve (Out-of-Sample begins 2020)")
    plt.ylabel("Growth of $1")
    plt.legend()
    plt.grid(True)

    plt.savefig(FIGURES_PATH / "equity_curve.png", dpi=150)
    plt.close()


def plot_drawdown(drawdown):
    plt.figure(figsize=(12,6))
    drawdown.plot()
    plt.title("Drawdown")
    plt.ylabel("Drawdown")
    plt.grid(True)

    plt.savefig(FIGURES_PATH / "drawdown.png", dpi=150)
    plt.close()
