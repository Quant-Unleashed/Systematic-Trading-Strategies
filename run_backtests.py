import pandas as pd
from pathlib import Path

from config.momentum_vol_regime_config import CONFIG

from src.data.data_loader import DataLoader
from src.strategies.strategy_factory import StrategyFactory
from src.backtest.backtester import Backtester
from src.analytics.performance import Performance
from src.analytics.oos_analysis import OOSAnalyzer
from src.utils.plotting import Plotter


def run_strategy(CONFIG):

    print("\n================ Strategy Configuration ================")

    for k, v in CONFIG.items():
        print(f"{k}: {v}")

    print("========================================================\n")

    # Load data
    loader = DataLoader(
        CONFIG["tickers"],
        CONFIG["start_date"],
        CONFIG["end_date"]
    )

    prices = loader.load()

    strategy = StrategyFactory.build(CONFIG)

    # Run backtest
    bt = Backtester(
        prices,
        strategy,
        transaction_cost=CONFIG["transaction_cost"]
    )

    returns = bt.run()

    # Equity curve
    equity = (1 + returns).cumprod()

    # ===== Performance Metrics =====

    total_return = Performance.total_return(returns)
    annual_return = Performance.annual_return(returns)
    vol = Performance.volatility(returns)
    sharpe = Performance.sharpe(returns)
    sortino = Performance.sortino(returns)
    calmar = Performance.calmar(returns)
    win_rate = Performance.win_rate(returns)
    max_dd = Performance.max_drawdown(equity)

    # OOS analysis
    analyzer = OOSAnalyzer(CONFIG["oos_date"])
    insample, oos = analyzer.split(returns)

    is_sharpe = Performance.sharpe(insample)
    oos_sharpe = Performance.sharpe(oos)

    print("\n================ Performance Summary ====================")

    print(f"Total Return: {total_return:.2%}")
    print(f"Annual Return: {annual_return:.2%}")
    print(f"Volatility: {vol:.2%}")
    print(f"Sharpe Ratio: {sharpe:.2f}")
    print(f"Sortino Ratio: {sortino:.2f}")
    print(f"Calmar Ratio: {calmar:.2f}")
    print(f"Max Drawdown: {max_dd:.2%}")
    print(f"Win Rate: {win_rate:.2%}")

    print("\n------ In-Sample / Out-of-Sample ------")

    print(f"IS Sharpe: {is_sharpe:.2f}")
    print(f"OOS Sharpe: {oos_sharpe:.2f}")

    print("=========================================================\n")

    # ===== Plot Results =====

    plotter = Plotter()

    plotter.equity_curve(equity)
    plotter.rolling_sharpe(returns)
    plotter.rolling_drawdown(equity)

    # ===== Save Results =====

    results = CONFIG.copy()

    results.update({
        "returns": returns,
        "equity": equity,

        "annual_return": annual_return,
        "volatility": vol,
        "sharpe": sharpe,
        "sortino": sortino,
        "calmar": calmar,
        "max_drawdown": max_dd,
        "win_rate": win_rate,
        "is_sharpe": is_sharpe,
        "oos_sharpe": oos_sharpe
    })

    Path("reports").mkdir(exist_ok=True)

    df = pd.DataFrame([results])

    df.to_csv("reports/last_strategy_run.csv", index=False)

    return results


if __name__ == "__main__":

    results = run_strategy(CONFIG)

    print("\nFinal Results Dictionary:")
    print(results)
