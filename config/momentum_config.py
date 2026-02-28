from config.base_config import BASE_CONFIG


CONFIG = {

    **BASE_CONFIG,

    "strategy": "momentum",

    "momentum_lookback": [21,63,252],

    "vol_target": None,

    "regime_filter": False

}
