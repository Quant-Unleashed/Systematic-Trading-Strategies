import yfinance as yf
import pandas as pd


class DataLoader:

    def __init__(self, tickers, start, end):
        self.tickers = tickers
        self.start = start
        self.end = end

    def load(self):

        data = yf.download(self.tickers, start=self.start, end=self.end)

        if "Adj Close" in data.columns:
            prices = data["Adj Close"]
        else:
            prices = data["Close"]

        prices = prices.dropna()

        return prices