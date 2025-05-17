import pandas as pd
import numpy as np
import yfinance as yf
from scipy.optimize import minimize

# Fetch data
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN"]
data = yf.download(tickers, start="2020-01-01", end="2025-01-01")["Adj Close"]
returns = data.pct_change().dropna()

# Mean-Variance Optimization
def portfolio_volatility(weights, returns, cov_matrix):
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))

def mean_variance_optimization(returns):
    n = len(returns.columns)
    cov_matrix = returns.cov()
    mean_returns = returns.mean() * 252
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple((0, 1) for _ in range(n))
    initial_weights = n * [1. / n]
    result = minimize(portfolio_volatility, initial_weights, args=(returns, cov_matrix),
                     method='SLSQP', bounds=bounds, constraints=constraints)
    return result.x

# Run optimization
optimal_weights = mean_variance_optimization(returns)
print("Optimal Weights:", dict(zip(tickers, optimal_weights)))
