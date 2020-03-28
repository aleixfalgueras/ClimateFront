################################################################################
# class: RouteState
################################################################################

class RouteState ():
    PENDING = "PENDING"
    PLANNED = "PLANNED"
    CANCELED = "CANCELED"

################################################################################
# mongo constants
################################################################################

class MongoCollection ():
    PRODUCT = "product"
    ROUTE = "route"

class MongoProductFields:
    ID = "id"
    NAME = "name"
    QUANTITY = "quantity"

class MongoRouteFields:
    ID = "id"
    STATE = "state"
    ORIGIN = "origin"
    DESTINY = "destiny"
    DEPARTURE = "departure"
    ARRIVAL = "arrival"
    PRODUCTS = "products"