RESEARCH_CONFIG = {

    "momentum_lookbacks": [
        [21],
        [63],
        [126],
        [252],
        [21,63,252]
    ],

    "vol_targets": [
        None,
        0.10,
        0.15
    ],

    "regime_filters": [
        False,
        True
    ],

    "portfolio_models": [
        "equal_weight",
        "inverse_vol",
        "mean_variance"
    ]

}
