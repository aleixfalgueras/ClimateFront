from src.api_rest.service.ProductService import getProducts, getProduct
from src.api_rest.utils import toJsonArray
from flask import Flask, jsonify

app = Flask (__name__)

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

    if  len (product) == 0: return jsonify ({"message": "Not found product with the id " + product_id})
    else:                   return jsonify (product[0].toJson ())

################################################################################
# Route
################################################################################


########################################################################################################################
###########################                            API REST                            #############################
########################################################################################################################

if __name__ == '__main__':
    app.run  (debug = True, port = 8080)