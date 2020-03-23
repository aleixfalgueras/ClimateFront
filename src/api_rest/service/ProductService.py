from src.mongo_adapter.MongoClientSingleton import MongoClientSingleton
from src.api_rest.model.Product import Product, toProduct
from src import config
from src.commons import MongoCollection, MongoProductFields


### function: getProduct ###

def getProduct (productId) :
    query = {MongoProductFields.ID : productId}
    res = MongoClientSingleton ().getDatabase (config.mongoDatabase).getCollection (MongoCollection.PRODUCT).find (query)

    return toProduct (res)

### function: getProducts ###

def getProducts ():
    res = MongoClientSingleton ().getDatabase (config.mongoDatabase).getCollection (MongoCollection.PRODUCT).find ({})

    return toProduct (res)