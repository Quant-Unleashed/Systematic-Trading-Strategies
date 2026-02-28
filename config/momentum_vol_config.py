from config.base_config import BASE_CONFIG


CONFIG = {

    **BASE_CONFIG,

    "strategy": "momentum_vol",

    "momentum_lookback": [21,63,252],

    "vol_target": 0.10,

    "regime_filter": False

}
