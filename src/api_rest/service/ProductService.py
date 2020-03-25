from src import config
from src.api_rest.utils import toProducts
from src.commons import MongoCollection, MongoProductFields
from src.mongo_adapter.MongoClientSingleton import MongoClientSingleton


### function: getProduct ###

def getProduct (productId) :
    query = {MongoProductFields.ID : productId}
    res = MongoClientSingleton ().getDatabase (config.mongoDatabase).getCollection (MongoCollection.PRODUCT).find (query)

    return toProducts (res)

### function: getProducts ###

def getProducts ():
    res = MongoClientSingleton ().getDatabase (config.mongoDatabase).getCollection (MongoCollection.PRODUCT).find ({})

    return toProducts (res)

### function: checkProductStock ###

def checkProductsStock (products):
    productCollection = MongoClientSingleton ().getDatabase (config.mongoDatabase).getCollection (MongoCollection.PRODUCT)

    for product in products:
        mongoProductsFind = productCollection.find ({MongoProductFields.ID : product.id})

        productsFind = toProducts (mongoProductsFind)

        if len (productsFind) == 0: return (False, product, 0) # product doesn't exist
        if int (product.quantity) > int (productsFind[0].quantity): return (False, product, 1) # no stock for the product

    return (True, None, None)

### function: decrementProductStock ###

def decrementProductsStock (products):
    productCollection = MongoClientSingleton ().getDatabase (config.mongoDatabase).getCollection (MongoCollection.PRODUCT)

    for product in products:
        mongoProductsFind = productCollection.find ({MongoProductFields.ID : product.id})
        productFind = toProducts (mongoProductsFind)[0]

        newQuantity = int (productFind.quantity) - int (product.quantity)

        productCollection.updateOneFieldById (product.id, MongoProductFields.QUANTITY, str (newQuantity))

### function: incrementProductsStock ###

def incrementProductsStock (products):
    productCollection = MongoClientSingleton ().getDatabase (config.mongoDatabase).getCollection (MongoCollection.PRODUCT)

    for product in products:
        mongoProductsFind = productCollection.find ({MongoProductFields.ID : product.id})
        productFind = toProducts (mongoProductsFind)[0]

        newQuantity = int (productFind.quantity) + int (product.quantity)
        productCollection.updateOneFieldById (product.id, MongoProductFields.QUANTITY, str (newQuantity))