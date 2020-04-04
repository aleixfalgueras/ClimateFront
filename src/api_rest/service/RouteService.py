import logging

from src.api_rest.model.entity.EntityRoute import EntityRoute
from src.api_rest.service.ProductService import modifyProductsStock
from src.api_rest.utils import toRoutes, toProducts, ProdutOperation
from src.commons import MongoCollection, MongoRouteFields, RouteState
from src.mongo_adapter.MongoClientSingleton import MongoClientSingleton


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

        modifyProductsStock (route.products, ProdutOperation.DECREMENT)

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

        modifyProductsStock (route.products, ProdutOperation.INCREMENT)

        return route

    except Exception as exc :
        logging.error ("RouteService: cancelRoute: Error canceling route: " + str (route))
        logging.error ("[Exception: " + str (exc) + "]")