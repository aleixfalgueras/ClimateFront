import time

from src.api_rest.model.entity.Entity import Entity
from src.commons import MongoRouteFields, RouteState


################################################################################
# class: EntityRoute
################################################################################

class EntityRoute (Entity) :

    ENTITY_NAME = "Route"


    ### function: __init__ ###

    def __init__ (self, origin, destiny, departure, arrival, products, strategy, id = None, state = RouteState.PENDING) :
        if id is None :
            self.id = str (time.time_ns ())
        else:
            self.id = id

        self.state = state
        self.origin = origin
        self.destiny = destiny
        self.departure = departure
        self.arrival = arrival
        self.products = products
        self.strategy = strategy

    ### function: __str__ ###

    def __str__ (self) :
        productsString = "\n"
        lastPosition = len (self.products) - 1

        for i in range (len (self.products)):
            if  i == lastPosition: productsString += str (self.products[i])
            else                 : productsString += str (self.products[i]) + "\n"


        return "Route (" + MongoRouteFields.ID +": " + self.id + ", " + \
               MongoRouteFields.STATE + ": " + self.state + ", " +  \
               MongoRouteFields.ORIGIN + ": " + self.origin + ", " + \
               MongoRouteFields.DESTINY + ": " + self.destiny + \
               MongoRouteFields.DEPARTURE + ": " + self.departure + ", " + \
               MongoRouteFields.ARRIVAL + ": " + self.arrival + ", " + \
               MongoRouteFields.PRODUCTS + ": " + productsString + \
               MongoRouteFields.STRATEGY + ": " + self.strategy.STRATEGY_NAME + ")"


    ### function: toJson ###

