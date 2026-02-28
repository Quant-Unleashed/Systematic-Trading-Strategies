import pandas as pd
import time


class WalkForwardOptimizer:

    def __init__(self, train_window=252*3, test_window=252):

        self.train_window = train_window
        self.test_window = test_window


    def run(self, prices, strategy_configs, backtest_fn):

        results = []

        start = self.train_window

        total_windows = int((len(prices) - self.train_window) / self.test_window)

        window_id = 1

        print("\n========== WALK FORWARD OPTIMIZATION ==========\n")

        while start < len(prices) - self.test_window:

            train = prices.iloc[start-self.train_window:start]
            test = prices.iloc[start:start+self.test_window]

            train_start = train.index[0]
            train_end = train.index[-1]

            test_start = test.index[0]
            test_end = test.index[-1]

            t0 = time.time()

            metrics = []

            # evaluate strategies
            for i, config in enumerate(strategy_configs):

                perf = backtest_fn(train, config)

                metrics.append((config, perf["sharpe"]))

            # select best strategy
            best_config, best_sharpe = max(metrics, key=lambda x: x[1])

            # test performance
            test_perf = backtest_fn(test, best_config)

            test_sharpe = test_perf["sharpe"]

            results.append(test_perf["returns"])

            elapsed = time.time() - t0

            # ----------- CLEAN SINGLE PRINT BLOCK -----------

            print(
                f"""
------------------------------------------------
Window {window_id}/{total_windows}

Train Period : {train_start.date()} → {train_end.date()}
Test Period  : {test_start.date()} → {test_end.date()}

Selected Strategy
  name      : {best_config['strategy']}
  lookback  : {best_config.get('momentum_lookback')}
  vol_target: {best_config.get('vol_target')}
  regime    : {best_config.get('regime_filter')}
  portfolio : {best_config.get('portfolio_model')}

Performance
  train sharpe : {best_sharpe:.2f}
  test sharpe  : {test_sharpe:.2f}

Window runtime: {elapsed:.2f}s
------------------------------------------------
"""
            )

            start += self.test_window

            window_id += 1

        print("\n========== WALK FORWARD COMPLETE ==========\n")

        return pd.concat(results)
