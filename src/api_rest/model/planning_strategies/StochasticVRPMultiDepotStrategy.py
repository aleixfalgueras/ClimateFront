################################################################################
# class: StochasticVRPMultiDepotStrategy
################################################################################

class StochasticVRPMultiDepotStrategy:

    STRATEGY_NAME = "StochasticVRPMultiDepotStrategy"


    ### function: __init__ ###

    def __init__ (self, route, forecasts) :
        self.route = route
        self.forecasts = forecasts


    ### function: planIt ###

    def planIt (self) :
        # do some stochastic VRP multi-depot stuff

        return "This a fancy plan"
