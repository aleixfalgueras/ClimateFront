import logging

from flask import Flask, jsonify, request

from src.api_rest.service.ProductService import getProducts, checkProductsStock
from src.api_rest.service.RouteService import getRoutes, addRoute, checkEditRoute, cancelRoute, addPlan, updateRoute
from src.api_rest.utils import toJsonArray, toProducts
from src.commons import MongoRouteFields, RouteState, MongoProductFields
from src.config import DevelopmentConfig

################################################################################
# app
################################################################################

app = Flask (__name__)


################################################################################
# BadRequest
################################################################################

class BadRequest (Exception) :
    def __init__(self, message, status = 400, payload = None):
        self.message = message
        self.status = status
        self.payload = payload

@app.errorhandler (BadRequest)
def handle_bad_request (error) :
    logging.error ("BadRequest: " + error.message)

    payload = dict (error.payload or ())

    payload ['status'] = error.status
    payload ['message'] = error.message

    return jsonify (payload), 400


################################################################################
# Product
################################################################################

### GET: get_products

@app.route ('/products')
def get_products () :
    args = request.args

    if len (args) == 0 :
        return jsonify (toJsonArray (getProducts ()))
    else:
        fieldsAllowed = MongoProductFields.ID + ", " + MongoProductFields.NAME + ", " + MongoProductFields.QUANTITY

        for k in args.keys () :
            if k != MongoProductFields.ID and k != MongoProductFields.NAME and k != MongoProductFields.QUANTITY:
                raise BadRequest ("Incorrect filter field: " + k  + ", allowed fields: " + fieldsAllowed, 400001)

        fields = {}

        if MongoProductFields.ID       in args : fields [MongoProductFields.ID]       = args [MongoProductFields.ID]
        if MongoProductFields.NAME     in args : fields [MongoProductFields.NAME]     = args [MongoProductFields.NAME]
        if MongoProductFields.QUANTITY in args : fields [MongoProductFields.QUANTITY] = args [MongoProductFields.QUANTITY]

        return jsonify (toJsonArray (getProducts (fields)))


### GET: get_product_by_id

@app.route ('/products/<string:product_id>')
def get_product_by_id (product_id) :
    product = getProducts ({MongoProductFields.ID : product_id})

    if  len (product) == 0 : raise BadRequest ("Product with id '" + product_id + "' not found", 400002)
    else :                   return jsonify (product[0].toJson ())


################################################################################
# Route
################################################################################

### GET: get_routes

@app.route ('/routes')
def get_routes () :
    args = request.args

    if len (args) == 0 :
        return jsonify (toJsonArray (getRoutes ()))
    else:
        fieldsAllowed = MongoRouteFields.ID + ", " + MongoRouteFields.STATE + ", " + MongoRouteFields.ORIGIN + ", " + \
                        MongoRouteFields.DESTINY + ", " + MongoRouteFields.DEPARTURE + ", " + MongoRouteFields.ARRIVAL + ", " + \
                        MongoRouteFields.STRATEGY

        for k in args.keys () :
            if k != MongoRouteFields.ID and k != MongoRouteFields.STATE and k != MongoRouteFields.ORIGIN and \
                k != MongoRouteFields.DESTINY and k != MongoRouteFields.DEPARTURE and k != MongoRouteFields.ARRIVAL and \
                   k != MongoRouteFields.STRATEGY :

                raise BadRequest ("Incorrect filter field: " + k + ", allowed fields: " + fieldsAllowed, 400101)

        fields = {}

        if MongoRouteFields.ID        in args : fields [MongoRouteFields.ID]        = args [MongoRouteFields.ID]
        if MongoRouteFields.STATE     in args : fields [MongoRouteFields.STATE]     = args [MongoRouteFields.STATE]
        if MongoRouteFields.ORIGIN    in args : fields [MongoRouteFields.ORIGIN]    = args [MongoRouteFields.ORIGIN]
        if MongoRouteFields.DESTINY   in args : fields [MongoRouteFields.DESTINY]   = args [MongoRouteFields.DESTINY]
        if MongoRouteFields.DEPARTURE in args : fields [MongoRouteFields.DEPARTURE] = args [MongoRouteFields.DEPARTURE]
        if MongoRouteFields.ARRIVAL   in args : fields [MongoRouteFields.ARRIVAL]   = args [MongoRouteFields.ARRIVAL]
        if MongoRouteFields.STRATEGY  in args : fields [MongoRouteFields.STRATEGY]  = args [MongoRouteFields.STRATEGY]

        return jsonify (toJsonArray (getRoutes (fields)))


### GET: PUT: get_route

@app.route ('/routes/<string:route_id>', methods = ["GET", "PUT"])
def get_route (route_id) :
    route = getRoutes ({MongoRouteFields.ID : route_id})

    if len (route) == 0 : raise BadRequest ("Route with id '" + route_id + "' not found", 400102)
    else :
        if request.method == "GET" : return jsonify (route [0].toJson ())
        else :
            if checkEditRoute (route [0]) :
                # Route.products isn't an upgradeable field, you must cancel the route and creat it again

                if request.json [MongoRouteFields.STATE] == RouteState.PLANNED : addPlan (route)

                routeUpdated = updateRoute (route [0],
                                            request.json [MongoRouteFields.ORIGIN],
                                            request.json [MongoRouteFields.DESTINY],
                                            request.json [MongoRouteFields.DEPARTURE],
                                            request.json [MongoRouteFields.ARRIVAL],
                                            request.json [MongoRouteFields.STRATEGY])


                return jsonify (routeUpdated.toJson)
            else :
                raise BadRequest ("Only can update routes with state '" + RouteState.PENDING + "'", 400105)



### POST: add_route

@app.route ("/routes/", methods = ["POST"])
def add_route () :
    (validStock, productError, errorCode) = checkProductsStock (toProducts (request.json [MongoRouteFields.PRODUCTS]))

    if validStock :
        # front-end must handle cities, date and strategy type validations

        route = addRoute (
            request.json [MongoRouteFields.ORIGIN],
            request.json [MongoRouteFields.DESTINY],
            request.json [MongoRouteFields.DEPARTURE],
            request.json [MongoRouteFields.ARRIVAL],
            request.json [MongoRouteFields.PRODUCTS],
            request.json [MongoRouteFields.STRATEGY]
        )

        return jsonify ({"message" : "Route created successful", "route" : route.toJson ()})

    else :
        if errorCode == 0 :
            raise BadRequest ("The product: " + str (productError) + " doesn't exist", 400103)
        else :
            raise BadRequest ("No stock for the product: " + str (productError), 400104)


### DELETE: delete_route

@app.route ('/routes/<string:route_id>', methods = ["DELETE"])
def cancel_route (route_id) :
    route = getRoutes ({MongoRouteFields.ID : route_id})

    if len (route) == 0 :
        return jsonify ({"message" : "Route with id '" + route_id + "' not found"})
    else :
        if checkEditRoute (route[0]):
            routeCanceled = cancelRoute (route[0])

            return jsonify ({"message" : "Route canceled successful", "route" : routeCanceled.toJson ()})
        else :
            raise BadRequest ("Only can cancel routes with state '" + RouteState.PENDING + "'", 400105)


########################################################################################################################
###########################                            API REST                            #############################
########################################################################################################################

if __name__ == '__main__':
    config = DevelopmentConfig ()
    logging.basicConfig (level = config.API_REST_LOG_LEVEL)
    app.run  (debug = True, port = config.API_REST_PORT)