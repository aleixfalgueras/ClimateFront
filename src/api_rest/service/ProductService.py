from src.api_rest.utils import toProducts
import logging

from src.api_rest.utils import toProducts
from src.commons import MongoCollection, MongoProductFields
from src.mongo_adapter.MongoClientSingleton import MongoClientSingleton


### function: getProducts ###

def getProducts (filters = None) :
    try :
        query = {}
        if filters is not None : query = filters

        logging.info ("ProductService: getProducts: filters: [" + str (filters) + "]")

        res = MongoClientSingleton ().getCollection (MongoCollection.PRODUCT).find (query)

        return toProducts (res)

    except Exception as exc :
        logging.error ("ProductService: getProducts: Error getting products, filters: " + str (filters))
        logging.error ("[Exception: " + str (exc) + "]")


### function: checkProductStock ###

def checkProductsStock (products) :
    try :
        productCollection = MongoClientSingleton ().getCollection (MongoCollection.PRODUCT)

        for product in products :
            mongoProductsFind = productCollection.find ({MongoProductFields.ID : product.id})

            productsFind = toProducts (mongoProductsFind)

            if len (productsFind) == 0 : return (False, product, 0)  # product doesn't exist
            if int (product.quantity) > int (productsFind [0].quantity) : return (False, product, 1)  # no stock for the product

        return (True, None, None)

    except Exception as exc :
        logging.error ("ProductService: checkProductsStock: Error checking products: " + products)
        logging.error ("[Exception: " + str (exc) + "]")


### function: decrementProductStock ###

def decrementProductsStock (products) :
    try :
        productCollection = MongoClientSingleton ().getCollection (MongoCollection.PRODUCT)

        for product in products :
            mongoProductsFind = productCollection.find ({MongoProductFields.ID : product.id})
            productFind = toProducts (mongoProductsFind) [0]

            newQuantity = int (productFind.quantity) - int (product.quantity)

            productCollection.updateOneFieldById (product.id, MongoProductFields.QUANTITY, str (newQuantity))

    except Exception as exc :
        logging.error ("ProductService: decrementProductsStock: Error decrementing products: " + products)
        logging.error ("[Exception: " + str (exc) + "]")


### function: incrementProductsStock ###

def incrementProductsStock (products) :
    try :
        productCollection = MongoClientSingleton ().getCollection (MongoCollection.PRODUCT)

        for product in products :
            mongoProductsFind = productCollection.find ({MongoProductFields.ID : product.id})
            productFind = toProducts (mongoProductsFind) [0]

            newQuantity = int (productFind.quantity) + int (product.quantity)
            productCollection.updateOneFieldById (product.id, MongoProductFields.QUANTITY, str (newQuantity))

    except Exception as exc :
        logging.error ("ProductService: incrementProductsStock: Error incrementing products: " + products)
        logging.error ("[Exception: " + str (exc) + "]")