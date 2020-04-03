from datetime import datetime


class StochasticVRPMultiDepotStrategy:

    STRATEGY_NAME = "StochasticVRPMultiDepotStrategy"

    def __init__ (self, route, forecasts):
        self.route = route
        self.forecasts = forecasts


    def planIt (self):
        # do some stochastic VRP multi-depot stuff

        return "This a fancy plan"
