from src.mongo_adapter.MongoClientSingleton import MongoClientSingleton
from src.api_rest.model.Product import Product
from src import config

### function: getProducts ###

def getProducts ():
    res = MongoClientSingleton ().getDatabase (config.mongoDatabase).getCollection ("product").find ({})

    products = []

    for r in res: products.append(Product (r['id'], r['name'], r['quantity']))

    return products