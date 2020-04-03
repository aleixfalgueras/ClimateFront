import logging

from src.api_rest.model.entity.EntityProduct import EntityProduct
from src.api_rest.model.entity.EntityRoute import EntityRoute
from src.commons import MongoProductFields, MongoRouteFields


### function: toJsonArray ###

def toJsonArray (entityList):
    try :
        jsonArray = []

        for entity in entityList : jsonArray.append (entity.toJson ())

        return jsonArray

    except Exception as exc :
        logging.error ("utils: toJsonArray: Error getting a JSON array for the entity '" + entityList [0].ENTITY_NAME)
        logging.error ("[Exception: " + str (exc) + "]")


### function: toProducts ###

def toProducts (mongoCursor) :
    try :
        products = []

        for product in mongoCursor :
            products.append (EntityProduct (
                product [MongoProductFields.ID],
                product [MongoProductFields.NAME],
                product [MongoProductFields.QUANTITY]
            ))

        return products

    except Exception as exc :
        logging.error ("utils: toProducts: Error parsing products from mongo to " + EntityProduct.ENTITY_NAME)
        logging.error ("[Exception: " + str (exc) + "]")


### function: toRoute ###

def toRoutes (mongoCursor):
    try:
        routes = []

        for route in mongoCursor :
            routes.append (EntityRoute (
                route [MongoRouteFields.ORIGIN],
                route [MongoRouteFields.DESTINY],
                route [MongoRouteFields.DEPARTURE],
                route [MongoRouteFields.ARRIVAL],
                toProducts (route [MongoRouteFields.PRODUCTS]),
                route [MongoRouteFields.STRATEGY],
                route [MongoRouteFields.ID],
                route [MongoRouteFields.STATE]
            ))

        return routes

    except Exception as exc:
        logging.error ("utils: toRoutes: Error parsing routes from mongo to " + EntityRoute.ENTITY_NAME)
        logging.error ("[Exception: " + str (exc) + "]")