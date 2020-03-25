from src import config
from src.api_rest.model.Route import Route
from src.api_rest.service.ProductService import incrementProductsStock, decrementProductsStock
from src.api_rest.utils import toRoutes, toProducts
from src.commons import MongoCollection, MongoRouteFields, RouteState
from src.mongo_adapter.MongoClientSingleton import MongoClientSingleton


### function: getRoute ###

def getRoute (routeId):
    query = {MongoRouteFields.ID: routeId}
    res = MongoClientSingleton ().getDatabase (config.mongoDatabase).getCollection (MongoCollection.ROUTE).find (query)

    return toRoutes (res)

### function: getRoutes ###

def getRoutes ():
    res = MongoClientSingleton ().getDatabase (config.mongoDatabase).getCollection (MongoCollection.ROUTE).find ({})

    return toRoutes (res)

### function: addRoute ###

def addRoute (origin, destiny, departure, arrival, productsMongo):
    route = Route (origin, destiny, departure, arrival, toProducts (productsMongo))

    routeCollection = MongoClientSingleton ().getDatabase (config.mongoDatabase).getCollection (MongoCollection.ROUTE)

    routeCollection.insertOne (route.toJson ())

    decrementProductsStock (route.products)

    return route

### function: checkCancelRoute ###

def checkCancelRoute (route):
    if  (route.state == RouteState.PENDING): return True
    else                                   : return False

### function: cancelRoute ###

def cancelRoute (route):
    route.state = RouteState.CANCELED

    routeCollection = MongoClientSingleton ().getDatabase (config.mongoDatabase).getCollection (MongoCollection.ROUTE)

    routeCollection.updateOneFieldById (route.id, MongoRouteFields.STATE, route.state)

    incrementProductsStock (route.products)

    return route