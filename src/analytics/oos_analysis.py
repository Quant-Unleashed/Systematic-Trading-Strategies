import pandas as pd


class OOSAnalyzer:

    def __init__(self, oos_date):
        self.oos_date = pd.to_datetime(oos_date)

    def split(self, returns):

        insample = returns[returns.index < self.oos_date]

        oos = returns[returns.index >= self.oos_date]

        return insample, oos