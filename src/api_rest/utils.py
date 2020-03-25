from src.api_rest.model.Product import Product
from src.api_rest.model.Route import Route
from src.commons import MongoProductFields, MongoRouteFields

### function: toJsonArray ###

def toJsonArray (entityList):
    jsonArray = []

    for entity in entityList: jsonArray.append (entity.toJson ())

    return jsonArray

### function: toProducts ###

def toProducts (mongoCursor) :
    products = []

    for product in mongoCursor:
        products.append (Product (
            product [MongoProductFields.ID],
            product [MongoProductFields.NAME],
            product [MongoProductFields.QUANTITY]
        ))

    return products

### function: toRoute ###

def toRoutes (mongoCursor):
    routes = []

    for route in mongoCursor:
        routes.append (Route (
            route [MongoRouteFields.ORIGIN],
            route [MongoRouteFields.DESTINY],
            route [MongoRouteFields.DEPARTURE],
            route [MongoRouteFields.ARRIVAL],
            toProducts (route [MongoRouteFields.PRODUCTS]),
            route [MongoRouteFields.ID],
            route [MongoRouteFields.STATE]
        ))

    return routes