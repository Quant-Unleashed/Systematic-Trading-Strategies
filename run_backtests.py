import yfinance as yf
import pandas as pd

from src.performance import performance_summary
from src.plotting import plot_equity_curve, plot_drawdown


print("Downloading data...")

# ETF universe (multi-asset)
tickers = ["SPY", "TLT", "GLD", "DBC"]

START_DATE = "2005-01-01"
END_DATE = "2025-12-31"
OOS_DATE = "2020-01-01"

data = yf.download(tickers, start=START_DATE, end=END_DATE)

# Use Adjusted Close if available, otherwise Close
if "Adj Close" in data.columns:
    prices = data["Adj Close"]
else:
    prices = data["Close"]

returns = prices.pct_change().dropna()

print("Running equal-weight portfolio backtest...")

# Equal-weight portfolio
portfolio_returns = returns.mean(axis=1)

summary, equity_curve, drawdown = performance_summary(portfolio_returns)

print("\nPerformance Summary:")
for k, v in summary.items():
    print(f"{k}: {v:.2%}")

print("Generating plots...")
plot_equity_curve(equity_curve)
plot_drawdown(drawdown)

print("Done! Check reports/figures/")
