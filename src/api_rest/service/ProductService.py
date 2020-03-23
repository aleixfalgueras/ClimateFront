from src.mongo_adapter.MongoClientSingleton import MongoClientSingleton
from src.api_rest.model.Product import toProduct
from src import config


### function: getProduct ###

def getProduct (productId) :
    query = {"id" : productId}
    res = MongoClientSingleton ().getDatabase (config.mongoDatabase).getCollection ("product").find (query)

    return toProduct (res)

### function: getProducts ###

def getProducts ():
    res = MongoClientSingleton ().getDatabase (config.mongoDatabase).getCollection ("product").find ({})

    return toProduct (res)