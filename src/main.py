from src import config
from src.mongo_adapter.MongoClientSingleton import MongoClientSingleton
from src.opcua_communication.ServerOPCUASimulation import ServerOPCUASimulation
from src.opcua_communication.ClientOPCUA import ClientOPCUA
from src.commons import MongoCollection, MongoRouteFields

import time

### function: mongoTest ###

def mongoTest ():
    mongoClient     = MongoClientSingleton ()
    climateFrontDb  = mongoClient.getDatabase (config.mongoDatabase)
    routeCollection = climateFrontDb.getCollection (MongoCollection.ROUTE)

    testRoute = {
        'id' : '1',
        'state' : 'PENDING',
        'origin' : 'London',
        'destiny' : 'Paris',
        'departure' : '20190105',
        'arrival' : '2019010',
        'products' :
        [
            {
                'name' : 'tomatoe',
                'quantity' : '5'
            },
            {
                'name' : 'banana',
                'quantity' : '50'
            }
        ]
    }
    routeCollection.insertOne (testRoute)

    res = routeCollection.find ({MongoRouteFields.ORIGIN : "London"})

    for r in res:
        print (r [MongoRouteFields.ORIGIN] + " - " + r [MongoRouteFields.DESTINY])

    mongoClient.close ()

### function: opcuaTest ###

def opcuaTest ():
    climateFrontDb = MongoClientSingleton  ().getDatabase (config.mongoDatabase)
    serverStock    = ServerOPCUASimulation ()

    serverStock.startSimulation ()
    serverStock.incrementStock ()

    clientStock = ClientOPCUA (config.serverOPCUASimulationEndpoint)

    varTomatoes = clientStock.getObjectsVar ("2:Stock", "2:Tomatoes")
    varBananas  = clientStock.getObjectsVar ("2:Stock", "2:Bananas")
    varApples   = clientStock.getObjectsVar ("2:Stock", "2:Apples")

    print ("Initial stock tomatoes: " + str (varTomatoes.get_value ()))
    print ("Initial stock bananas: "  + str (varBananas.get_value ()))
    print ("Initial stock apples: "   + str (varApples.get_value ()))

    clientStock.subscribeVarToMongoCollection (varTomatoes, climateFrontDb, MongoCollection.PRODUCT)
    clientStock.subscribeVarToMongoCollection (varBananas, climateFrontDb, MongoCollection.PRODUCT)
    clientStock.subscribeVarToMongoCollection (varApples, climateFrontDb, MongoCollection.PRODUCT)

    serverStock.incrementStock ()

    print ("Final stock tomatoes: " + str (varTomatoes.get_value ()))
    print ("Final stock bananas: "  + str (varBananas.get_value ()))
    print ("Final stock apples: "   + str (varApples.get_value ()))


########################################################################################################################
#########################                            CLIMATE FRONT                            ##########################
########################################################################################################################

if __name__ == '__main__':

    mongoTest ()
    opcuaTest ()

    while True:
        time.sleep (100000)
