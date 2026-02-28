import pandas as pd
import yfinance as yf
from pathlib import Path


class DataLoader:

    def __init__(self, tickers, start, end):

        self.tickers = sorted(tickers)
        self.start = start
        self.end = end

        ticker_str = "_".join(self.tickers)

        filename = f"prices_{ticker_str}_{start}_{end}.csv"

        self.cache_file = Path("data/processed") / filename

    def load(self):

        if self.cache_file.exists():

            print("Using cached dataset")

            prices = pd.read_csv(
                self.cache_file,
                index_col=0,
                parse_dates=True
            )

            return prices

        print("Downloading data from Yahoo Finance")

        data = yf.download(
            self.tickers,
            start=self.start,
            end=self.end,
            auto_adjust=True
        )

        # Handle both single and multi index outputs
        if isinstance(data.columns, pd.MultiIndex):

            prices = data["Close"]

        else:

            prices = data

        prices = prices.dropna(how="all")

        self.cache_file.parent.mkdir(parents=True, exist_ok=True)

        prices.to_csv(self.cache_file)

        return prices
