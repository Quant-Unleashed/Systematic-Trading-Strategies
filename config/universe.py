UNIVERSE = {

    "equities_us": {
        "benchmark": "SPY",
        "tickers": [
            "SPY","QQQ","IWM","DIA",
            "XLK","XLF","XLE","XLV","XLY","XLI"
        ]
    },

    "equities_international": {
        "benchmark": "EFA",
        "tickers": [
            "EFA","EEM","EWJ","EWG","EWU","EWZ"
        ]
    },

    "fixed_income": {
        "benchmark": "AGG",
        "tickers": [
            "TLT","IEF","SHY","TIP","LQD","HYG","BND"
        ]
    },

    "commodities": {
        "benchmark": "DBC",
        "tickers": [
            "GLD","SLV","DBC","USO","UNG","DBA"
        ]
    },

    "currencies": {
        "benchmark": "UUP",
        "tickers": [
            "UUP","FXE","FXY","FXB","FXA","FXC"
        ]
    },

    "real_assets": {
        "benchmark": "VNQ",
        "tickers": [
            "VNQ","REET","REM"
        ]
    }
}


ALL_TICKERS = []

for asset_class in UNIVERSE.values():
    ALL_TICKERS += asset_class["tickers"]
