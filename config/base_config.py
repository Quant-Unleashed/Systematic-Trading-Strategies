from config.universe import ALL_TICKERS

BASE_CONFIG = {

    # universe
    "tickers": ALL_TICKERS,

    # data range
    "start_date": "2005-01-01",
    "end_date": "2025-12-31",

    # backtest settings
    "transaction_cost": 0.0005,
    "rebalance": "monthly",

    # research settings
    "oos_date": "2020-01-01",

    # portfolio construction
    "portfolio_model": "equal_weight",

    # risk controls
    "risk_scaling": True
}
