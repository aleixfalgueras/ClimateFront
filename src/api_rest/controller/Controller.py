from flask import Flask, jsonify, request

from src.api_rest.service.ProductService import getProducts, getProduct, checkProductsStock
from src.api_rest.service.RouteService import getRoutes, getRoute, addRoute, checkCancelRoute, cancelRoute
from src.api_rest.utils import toJsonArray, toProducts
from src.commons import MongoRouteFields, RouteState
from src.config import DevelopmentConfig

app = Flask (__name__)

################################################################################
# BadRequest
################################################################################

class BadRequest (Exception):
    def __init__(self, message, status = 400, payload = None):
        self.message = message
        self.status = status
        self.payload = payload

@app.errorhandler (BadRequest)
def handle_bad_request (error):
    payload = dict (error.payload or ())

    payload ['status'] = error.status
    payload ['message'] = error.message

    return jsonify (payload), 400

################################################################################
# Product
################################################################################

### GET: get_products

@app.route ('/products')
def get_products ():
    return jsonify (toJsonArray (getProducts ()))

### GET: get_product

@app.route ('/products/<string:product_id>')
def get_product (product_id):
    product = getProduct (product_id)

    if  len (product) == 0 : raise BadRequest ("Product with id: " + product_id + " not found", 400001)
    else                   : return jsonify (product[0].toJson ())

################################################################################
# Route
################################################################################

### GET: get_routes

@app.route ('/routes')
def get_routes ():
    return jsonify (toJsonArray (getRoutes ()))

### GET: get_route

@app.route ('/routes/<string:route_id>')
def get_route (route_id):
    route = getRoute (route_id)

    if  len (route) == 0: raise BadRequest ("Route with id: " + route_id + " not found", 400101)
    else:                 return jsonify (route[0].toJson ())

### POST: add_route

@app.route ("/routes/", methods = ["POST"])
def add_route ():
    (validStock, productError, errorCode) = checkProductsStock (toProducts (request.json [MongoRouteFields.PRODUCTS]))

    if validStock:
        route = addRoute (
            request.json [MongoRouteFields.ORIGIN],
            request.json [MongoRouteFields.DESTINY],
            request.json [MongoRouteFields.DEPARTURE],
            request.json [MongoRouteFields.ARRIVAL],
            request.json [MongoRouteFields.PRODUCTS]
        )

        return jsonify ({"message" : "Route created successful", "route" : route.toJson ()})

    else:
        if errorCode == 0:
            raise BadRequest ("The product: " + str (productError) + " doesn't exist", 400102)
        else:
            raise BadRequest ("No stock for the product: " + str (productError), 400103)

### DELETE: delete_route
@app.route ('/routes/<string:route_id>', methods = ["DELETE"])
def cancel_route (route_id):
    route = getRoute (route_id)

    if len (route) == 0: raise BadRequest ("Route with id: " + route_id + " not found", 400101)
    else:
        if checkCancelRoute (route[0]):
            routeCanceled = cancelRoute (route[0])

            return jsonify ({"message" : "Route canceled successful", "route" : routeCanceled.toJson ()})
        else:
            raise BadRequest ("Only can cancel routes with state " + RouteState.PENDING, 400104)


########################################################################################################################
###########################                            API REST                            #############################
########################################################################################################################

if __name__ == '__main__':
    config = DevelopmentConfig ()
    app.run  (debug = True, port = config.apiRestPort)