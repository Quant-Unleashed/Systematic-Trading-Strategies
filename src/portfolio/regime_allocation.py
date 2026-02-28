class RegimeAllocation:

    def __init__(self, risk_assets, defensive_assets):

        self.risk_assets = risk_assets
        self.defensive_assets = defensive_assets

    def allocate(self, regime):

        weights = {}

        if regime == 1:

            for a in self.risk_assets:
                weights[a] = 1/len(self.risk_assets)

        else:

            for a in self.defensive_assets:
                weights[a] = 1/len(self.defensive_assets)

        return weights
