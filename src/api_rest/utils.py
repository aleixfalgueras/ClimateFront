import logging

from src.api_rest.model.EntityProduct import Product
from src.api_rest.model.EntityRoute import Route
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
            products.append (Product (
                product [MongoProductFields.ID],
                product [MongoProductFields.NAME],
                product [MongoProductFields.QUANTITY]
            ))

        return products

    except Exception as exc :
        logging.error ("utils: toProducts: Error parsing products from mongo to " + Product.ENTITY_NAME)
        logging.error ("[Exception: " + str (exc) + "]")


### function: toRoute ###

def toRoutes (mongoCursor):
    try:
        routes = []

        for route in mongoCursor :
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

    except Exception as exc:
        logging.error ("utils: toRoutes: Error parsing routes from mongo to " + Route.ENTITY_NAME)
        logging.error ("[Exception: " + str (exc) + "]")