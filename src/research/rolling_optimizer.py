import pandas as pd


class RollingOptimizer:

    def __init__(self, window=252):

        self.window = window


    def select_best(self, strategy_results):

        best_params = []

        for t in range(self.window, len(strategy_results)):

            past = strategy_results.iloc[t-self.window:t]

            best = past.mean().idxmax()

            best_params.append(best)

        return best_params
