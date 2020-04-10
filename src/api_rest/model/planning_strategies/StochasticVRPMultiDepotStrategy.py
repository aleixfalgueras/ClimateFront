from src.api_rest.model.entity.EntityPlan import EntityPlan
from src.api_rest.model.planning_strategies.Strategy import Strategy
from src.services.openWeatherMap.OpenWeatherMap import getCityForecast


################################################################################
# class: StochasticVRPMultiDepotStrategy
################################################################################

class StochasticVRPMultiDepotStrategy (Strategy) :

    STRATEGY_NAME = "StochasticVRPMultiDepotStrategy"


    ### function: planIt ###

    def planIt (self, route) :
        # for the moment we only one use forecasts for the source and destiny places

        locationForecastsUsed = [getCityForecast (route.origin), getCityForecast (route.destiny)]

        # do some stochastic VRP multi-depot stuff

        plan = EntityPlan (route, "This is a fancy plan", locationForecastsUsed)

        return plan