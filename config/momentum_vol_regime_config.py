from config.base_config import CONFIG as BASE

CONFIG = BASE.copy()

CONFIG.update({

    "strategy": "momentum",

    "momentum_lookback": 252,

    "vol_target": 0.10,

    "regime_filter": True

})