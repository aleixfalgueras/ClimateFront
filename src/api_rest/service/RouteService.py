import logging

from src.api_rest.model.EntityRoute import Route
from src.api_rest.service.ProductService import incrementProductsStock, decrementProductsStock
from src.api_rest.utils import toRoutes, toProducts
from src.commons import MongoCollection, MongoRouteFields, RouteState
from src.mongo_adapter.MongoClientSingleton import MongoClientSingleton


### function: getRoutes ###

def getRoutes (fields = dict()):
    try :
        query = {}
        if fields is not None : query = fields

        res = MongoClientSingleton ().getCollection (MongoCollection.ROUTE).find (query)

        return toRoutes (res)

    except Exception as exc :
        logging.error ("RouteService: getRoutes: Error getting routes, fields: " + str (fields))
        logging.error ("[Exception: " + str (exc) + "]")


### function: addRoute ###

def addRoute (origin, destiny, departure, arrival, productsMongo):
    try :
        route = Route (origin, destiny, departure, arrival, toProducts (productsMongo))

        MongoClientSingleton ().getCollection (MongoCollection.ROUTE).insertOne (route.toJson ())

        decrementProductsStock (route.products)

        return route

    except Exception as exc :
        logging.error ("RouteService: addRoute: Error addind route. Params: " + origin + ", " + destiny + ", " + \
                       departure + ", " + arrival + ", " + productsMongo)
        logging.error ("[Exception: " + str (exc) + "]")


### function: checkCancelRoute ###

def checkCancelRoute (route):
    if  (route.state == RouteState.PENDING): return True
    else                                   : return False


### function: cancelRoute ###

def cancelRoute (route):
    try :
        route.state = RouteState.CANCELED

        MongoClientSingleton ().getCollection (MongoCollection.ROUTE)\
            .updateOneFieldById (route.id, MongoRouteFields.STATE, route.state)

        incrementProductsStock (route.products)

        return route

    except Exception as exc :
        logging.error ("RouteService: cancelRoute: Error canceling route: " + str (route))
        logging.error ("[Exception: " + str (exc) + "]")