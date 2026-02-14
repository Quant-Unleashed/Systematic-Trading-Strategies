import matplotlib.pyplot as plt
from pathlib import Path


FIGURES_PATH = Path("reports/figures")
FIGURES_PATH.mkdir(parents=True, exist_ok=True)


def plot_equity_curve(equity_curve):
    plt.figure(figsize=(10,5))
    equity_curve.plot()
    plt.title("Portfolio Equity Curve")
    plt.ylabel("Growth of $1")
    plt.grid(True)
    plt.savefig(FIGURES_PATH / "equity_curve.png")
    plt.close()


def plot_drawdown(drawdown):
    plt.figure(figsize=(10,5))
    drawdown.plot()
    plt.title("Drawdown")
    plt.ylabel("Drawdown")
    plt.grid(True)
    plt.savefig(FIGURES_PATH / "drawdown.png")
    plt.close()
