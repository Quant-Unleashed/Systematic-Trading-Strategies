import matplotlib.pyplot as plt
from pathlib import Path
from src.analytics.performance import Performance


class Plotter:

    def __init__(self):
        self.path = Path("reports/figures")
        self.path.mkdir(parents=True, exist_ok=True)

    def equity_curve(self, equity):

        plt.figure(figsize=(10,5))
        equity.plot()
        plt.title("Equity Curve")
        plt.grid(True)
        plt.savefig(self.path / "equity_curve.png")
        plt.close()

    def rolling_sharpe(self, returns):

        rs = Performance.rolling_sharpe(returns)

        plt.figure(figsize=(10,5))
        rs.plot()
        plt.title("Rolling Sharpe (1Y)")
        plt.grid(True)
        plt.savefig(self.path / "rolling_sharpe.png")
        plt.close()

    def rolling_drawdown(self, equity):

        dd = Performance.rolling_drawdown(equity)

        plt.figure(figsize=(10,5))
        dd.plot()
        plt.title("Rolling Drawdown")
        plt.grid(True)
        plt.savefig(self.path / "rolling_drawdown.png")
        plt.close()
