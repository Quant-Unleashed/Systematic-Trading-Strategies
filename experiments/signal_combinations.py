from config.momentum_config import CONFIG as MOM
from config.momentum_vol_config import CONFIG as MOM_VOL
from config.momentum_vol_regime_config import CONFIG as FULL


SCENARIOS = {

    "Momentum": MOM,

    "Momentum + Vol Target": MOM_VOL,

    "Momentum + Vol + Regime": FULL

}