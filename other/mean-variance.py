import pandas as pd
import numpy as np
from scipy.optimize import minimize
import yfinance as yf

data1 = yf.download("AAPL", start= '2025-08-18', end= '2025-08-21',interval="1m")['Close']

# Fetch data with error handling
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN"]
data = pd.DataFrame()
for i in tickers:
    df = pd.read_csv('stocks/' + i + '.csv')
    df.index = pd.to_datetime(df['Date'])
    data[i] = df['Adj Close'].loc["2018-01-01":"2019-01-01"]

# Calculate returns, drop missing data
returns = data.pct_change().dropna()

# Mean-Variance Optimization
def portfolio_volatility(weights, returns, cov_matrix):
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))

def mean_variance_optimization(ret):
    n = len(ret.columns)
    cov_matrix = ret.cov()
    mean_returns = ret.mean() * 252
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple((0, 1) for _ in range(n))
    initial_weights = n * [1. / n]
    result = minimize(portfolio_volatility, initial_weights, args=(ret, cov_matrix),
                      method='SLSQP', bounds=bounds, constraints=constraints)
    return result.x

# Run optimization
optimal_weights = mean_variance_optimization(returns)
print("Optimal Weights:", dict(zip(tickers, optimal_weights)))
