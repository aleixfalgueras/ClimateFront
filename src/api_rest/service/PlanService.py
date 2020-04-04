import logging

from src.api_rest.model.entity.EntityPlan import EntityPlan
from src.api_rest.model.planning_strategies.StochasticVRPMultiDepotStrategy import StochasticVRPMultiDepotStrategy
from src.api_rest.utils import toPlans
from src.commons import MongoCollection
from src.mongo_adapter.MongoClientSingleton import MongoClientSingleton
from src.services.openWeatherMap.OpenWeatherMap import getCityForecast


### function: getPlans ###

def getPlans (filters = None) :
    try :
        query = {}
        if filters is not None : query = filters

        logging.info ("PlansService: getPlans: filters: [" + str (filters) + "]")

        res = MongoClientSingleton ().getCollection (MongoCollection.PLAN).find (query)

        return toPlans (res)

    except Exception as exc :
        logging.error ("PlanService: getPlans: Error getting plans, filters: " + str (filters))
        logging.error ("[Exception: " + str (exc) + "]")


### function: addPlan ###

def addPlan (route):
    try :
        # for the moment we only one use forecasts for the source and destiny places
        locationForecastsUsed = [getCityForecast (route.origin), getCityForecast (route.destiny)]

        if route.strategy == StochasticVRPMultiDepotStrategy.STRATEGY_NAME :
            strategy = StochasticVRPMultiDepotStrategy (route, locationForecastsUsed)
        else :
            raise Exception ("Unknow strategy '" + route.strategy + "'")

        plan = EntityPlan (route, strategy.planIt (), locationForecastsUsed)

        MongoClientSingleton ().getCollection (MongoCollection.PLAN).insertOne (plan.toJson ())

        return plan

    except Exception as exc :
        logging.error ("PlanService: addPlan: Error creating plan for the route: " + str (route))
        logging.error ("[Exception: " + str (exc) + "]")