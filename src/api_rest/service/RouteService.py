import logging

from src.api_rest.model.entity.EntityRoute import EntityRoute
from src.api_rest.service.ProductService import incrementProductsStock, decrementProductsStock
from src.api_rest.utils import toRoutes, toProducts
from src.commons import MongoCollection, MongoRouteFields, RouteState
from src.mongo_adapter.MongoClientSingleton import MongoClientSingleton
from src.api_rest.model.entity.EntityPlan import EntityPlan
from src.api_rest.model.planning_strategies.StochasticVRPMultiDepotStrategy import StochasticVRPMultiDepotStrategy
from src.services.openWeatherMap.OpenWeatherMap import getForecast

### function: getRoutes ###

def getRoutes (filters = None) :
    try :
        query = {}
        if filters is not None : query = filters

        logging.info ("RouteService: getRoutes: filters: [" + str (filters) + "]")

        res = MongoClientSingleton ().getCollection (MongoCollection.ROUTE).find (query)

        return toRoutes (res)

    except Exception as exc :
        logging.error ("RouteService: getRoutes: Error getting routes, filters: " + str (filters))
        logging.error ("[Exception: " + str (exc) + "]")


### function: addRoute ###

def addRoute (origin, destiny, departure, arrival, productsMongo, strategy) :
    try :
        route = EntityRoute (origin, destiny, departure, arrival, toProducts (productsMongo), strategy)

        MongoClientSingleton ().getCollection (MongoCollection.ROUTE).insertOne (route.toJson ())

        decrementProductsStock (route.products)

        return route

    except Exception as exc :
        logging.error ("RouteService: addRoute: Error addind route. Params: " + origin + ", " + destiny + ", " + \
                       departure + ", " + arrival + ", " + productsMongo)
        logging.error ("[Exception: " + str (exc) + "]")


### function: checkEditRoute ###

def checkEditRoute (route) :
    if  (route.state == RouteState.PENDING): return True
    else                                   : return False

### function: updateRoute ###

def updateRoute (originalRoute, fieldsToUpdate):
    MongoClientSingleton ().getCollection (MongoCollection.ROUTE).updateOneById (originalRoute.id, fieldsToUpdate)

    return getRoutes ({MongoRouteFields.ID : originalRoute.id}) [0]

### function: cancelRoute ###

def cancelRoute (route) :
    try :
        route.state = RouteState.CANCELED

        MongoClientSingleton ().getCollection (MongoCollection.ROUTE)\
            .updateOneFieldById (route.id, MongoRouteFields.STATE, route.state)

        incrementProductsStock (route.products)

        return route

    except Exception as exc :
        logging.error ("RouteService: cancelRoute: Error canceling route: " + str (route))
        logging.error ("[Exception: " + str (exc) + "]")


### function: addPlan ###

def addPlan (route):
    try :
        # for the moment we only one use forecasts for the source and destiny places
        locationForecastsUsed = [getForecast (route.origin), getForecast (route.destiny)]

        strategy = None

        if route.strategy == StochasticVRPMultiDepotStrategy.STRATEGY_NAME:
            strategy = StochasticVRPMultiDepotStrategy (route, locationForecastsUsed)
        else:
            raise Exception ("Unknow strategy '" + route.strategy + "'")

        plan = EntityPlan (route, strategy.planIt (), locationForecastsUsed)

        MongoClientSingleton ().getCollection (MongoCollection.PLAN).insertOne (plan.toJson ())

        return plan

    except Exception as exc :
        logging.error ("RouteService: addPlan: Error creating plan for the route: " + str (route))
        logging.error ("[Exception: " + str (exc) + "]")