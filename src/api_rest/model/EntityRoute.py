import time

from src.commons import MongoRouteFields, RouteState


################################################################################
# class: Route
################################################################################

class Route:

    entityName = "Route"


    ### function: __init__ ###

    def __init__ (self, origin, destiny, departure, arrival, products, id = None, state = RouteState.PENDING):
        if id is None:
            self.id = str (time.time_ns ())
        else:
            self.id = id

        self.state = state
        self.origin = origin
        self.destiny = destiny
        self.departure = departure
        self.arrival = arrival
        self.products = products


    ### function: __str__ ###

    def __str__ (self):
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
               MongoRouteFields.PRODUCTS + ": " + productsString + ")"


    ### function: toJson ###

    def toJson (self):
        products = []

        for product in self.products: products.append (product.toJson ())

        return {
            MongoRouteFields.ID : self.id,
            MongoRouteFields.STATE : self.state,
            MongoRouteFields.ORIGIN : self.origin,
            MongoRouteFields.DESTINY : self.destiny,
            MongoRouteFields.DEPARTURE : self.departure,
            MongoRouteFields.ARRIVAL : self.arrival,
            MongoRouteFields.PRODUCTS : products
        }