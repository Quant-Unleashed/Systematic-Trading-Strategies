from config.base_config import CONFIG as BASE

CONFIG = BASE.copy()

CONFIG.update({

    "strategy": "momentum",

    "momentum_lookback": 252,

    "vol_target": None,

    "regime_filter": False

})