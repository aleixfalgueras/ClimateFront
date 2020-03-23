from src.api_rest.service.ProductService import getProducts
from src.api_rest.utils import toJsonArray
from flask import Flask, jsonify

app = Flask (__name__)

################################################################################
# Product
################################################################################

### GET

@app.route ('/products')
def get_products ():
    prodcuts = getProducts ()

    return jsonify (toJsonArray (prodcuts))


########################################################################################################################
###########################                            API REST                            #############################
########################################################################################################################

if __name__ == '__main__':
    app.run  (debug = True, port = 8080)