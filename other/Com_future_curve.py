import matplotlib
matplotlib.use('TkAgg')

import yfinance as yf
import datetime
from datetime import date, timedelta
import matplotlib.pyplot as plt

# Month codes for futures contracts
month_codes = 'FGHJKMNQUVXZ'


def get_month_code(month):
    return month_codes[month - 1]


def next_month(year, month):
    month += 1
    if month > 12:
        month = 1
        year += 1
    return year, month


def get_expiration_date(delivery_year, delivery_month):
    # Calculate the preceding month
    prec_year = delivery_year if delivery_month > 1 else delivery_year - 1
    prec_month = delivery_month - 1 if delivery_month > 1 else 12

    # 25th of the preceding month
    day25 = date(prec_year, prec_month, 25)

    # Find the 3rd business day prior (skipping weekends; holidays not considered for simplicity)
    count = 0
    current = day25
    while count < 3:
        current -= timedelta(days=1)
        if current.weekday() < 5:  # Monday to Friday
            count += 1
    return current


# Get today's date
today = date.today()

# Start from current year and month
current_year = today.year
current_month = today.month

tickers = []
num_contracts = 24  # Number of future contracts to fetch
ticker_com = 'CL'

while len(tickers) < num_contracts:
    exp_date = get_expiration_date(current_year, current_month)
    if exp_date >= today:
        month_code = get_month_code(current_month)
        year_two_digit = current_year % 100
        ticker = f'{ticker_com}{month_code}{year_two_digit:02d}.NYM'
        tickers.append(ticker)
    current_year, current_month = next_month(current_year, current_month)

# Download data starting from yesterday (adjust if needed for weekends/markets)
yesterday = today - timedelta(days=4)

date = yesterday
data = yf.download(tickers, start=date)['Close']

# Get the latest close prices in order
# close_prices = data.iloc[-1].tolist()  # Assumes columns are in ticker order
close_prices = [data[i].iloc[-1] for i in tickers]
close_prices1 = [data[i].iloc[-2] for i in tickers]
close_prices2 = [data[i].iloc[-3] for i in tickers]
close_prices3 = [data[i].iloc[-4] for i in tickers]


# Plot the data
contracts = [ticker.split('.')[0] for ticker in tickers]
plt.figure(figsize=(10, 6))
plt.plot(contracts, close_prices, marker='o')
plt.plot(contracts, close_prices1, marker='o')
plt.plot(contracts, close_prices2, marker='o')
plt.plot(contracts, close_prices3, marker='o')
plt.xlabel('Contract')
plt.ylabel('Close Price')
plt.title(f'{ticker_com} Futures Forward Curve')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()