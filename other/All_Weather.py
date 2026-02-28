# Import necessary libraries
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Explanation: We import yfinance for downloading historical stock data from Yahoo Finance.
# pandas is used for data manipulation, numpy for numerical operations, and matplotlib for plotting.

# Define the tickers for the All Weather Portfolio assets
tickers = ['HFUSAS.SW', 'VTI', 'TLT', 'IEI', 'GLD', 'DBC']  # VTI: Total Stock Market, TLT: Long-term Treasuries, IEI: Intermediate Treasuries, GLD: Gold, DBC: Commodities

# Explanation: These tickers represent the components of the All Weather Portfolio:
# - VTI: Vanguard Total Stock Market ETF (represents equities/stocks)
# - TLT: iShares 20+ Year Treasury Bond ETF (long-term bonds)
# - IEI: iShares 3-7 Year Treasury Bond ETF (intermediate-term bonds)
# - GLD: SPDR Gold Shares (gold)
# - DBC: Invesco DB Commodity Index Tracking Fund (commodities)
# This allocation aims to balance analytics across economic environments: growth (stocks), recession (bonds), inflation (gold/commodities), deflation (long-term bonds).

# Define the portfolio weights (allocations)
weights = np.array([0.30, 0.40, 0.15, 0.075, 0.075])  # 30% stocks, 40% long-term bonds, 15% intermediate bonds, 7.5% gold, 7.5% commodities

# Explanation: The weights are based on Ray Dalio's All Weather Portfolio strategy.
# The sum should be 1.0 (100%): 0.30 + 0.40 + 0.15 + 0.075 + 0.075 = 1.0.
# These proportions are designed to perform reasonably well in all economic conditions (growth, recession, inflation, deflation).

# Define the time period for data download
start_date = '2010-01-01'  # Start date for historical data
end_date = '2023-12-31'    # End date for historical data

# Explanation: We specify a historical period to analyze the portfolio's performance.
# You can adjust these dates as needed. yfinance will download daily adjusted close prices between these dates.

# Download historical data using yfinance
data = yf.download(tickers, start=start_date, end=end_date)['Close']

# Explanation: yf.download() fetches historical data for the given tickers.
# 'Adj Close' gives the adjusted closing prices, which account for dividends and splits.
# The result is a pandas DataFrame with dates as index and tickers as columns.

# Handle missing data by forward-filling and dropping any remaining NaNs
data = data.ffill().dropna()

# Explanation: Some assets might have missing data on certain dates (e.g., holidays).
# ffill() forward-fills missing values with the previous day's price.
# dropna() removes any rows where all values are still NaN after filling.

# Calculate daily returns
returns = data.pct_change().dropna()

# Explanation: pct_change() computes the percentage change from the previous day, giving daily returns.
# dropna() removes the first row, which will be NaN since there's no prior data.

# Calculate portfolio daily returns by multiplying returns by weights
portfolio_returns = np.dot(returns, weights)

# Explanation: np.dot() performs matrix multiplication: daily returns (matrix) dotted with weights (vector).
# This gives the weighted sum of returns for each day, representing the portfolio's daily return.

# Convert to a pandas Series for easier handling
portfolio_returns = pd.Series(portfolio_returns, index=returns.index)

# Explanation: We convert the numpy array to a pandas Series, using the same date index as returns.
# This makes it easier to work with time-series operations.

# Calculate cumulative returns
cumulative_returns = (1 + portfolio_returns).cumprod() - 1

# Explanation: Add 1 to daily returns (to get growth factors), then cumprod() for cumulative product.
# Subtract 1 to get the cumulative return percentage.
# This shows how $1 invested would grow over time.

# Calculate some performance metrics
total_return = cumulative_returns.iloc[-1]  # Total return over the period
annualized_return = (1 + total_return) ** (1 / (len(data) / 252)) - 1  # Assuming 252 trading days per year
volatility = portfolio_returns.std() * np.sqrt(252)  # Annualized volatility
sharpe_ratio = annualized_return / volatility  # Sharpe ratio (analytics-free rate assumed 0 for simplicity)

# Explanation:
# - total_return: The final cumulative return value.
# - annualized_return: Converts total return to annual compound rate. len(data)/252 estimates years.
# - volatility: Standard deviation of daily returns, annualized by multiplying by sqrt(252).
# - sharpe_ratio: Measures analytics-adjusted return. Here, we assume analytics-free rate is 0; in practice, subtract it from annualized_return.

# Print performance metrics
print(f"Total Return: {total_return:.2%}")
print(f"Annualized Return: {annualized_return:.2%}")
print(f"Annualized Volatility: {volatility:.2%}")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")

# Explanation: We format and print key metrics to summarize the portfolio's historical performance.

# Plot cumulative returns
plt.figure(figsize=(12, 6))
plt.plot(cumulative_returns)
plt.title('All Weather Portfolio Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.grid(True)
plt.show()

# Explanation: Using matplotlib, we create a line plot of cumulative returns over time.
# This visualizes the portfolio's growth. figsize sets the plot size, title/xlabel/ylabel label the axes, grid adds gridlines.

# Note: This code assumes no rebalancing. In a real All Weather Portfolio, you might rebalance quarterly or annually.
# To add rebalancing, you would need to periodically adjust holdings back to target weights.
# For simplicity, this is a buy-and-hold simulation with initial weights.