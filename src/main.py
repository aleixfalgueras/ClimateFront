from src.config import DevelopmentConfig
from src.mongo_adapter.MongoClientSingleton import MongoClientSingleton
from src.opcua_communication.ServerOPCUASimulation import ServerOPCUASimulation
from src.opcua_communication.ClientOPCUA import ClientOPCUA

import time
import logging

### function: mongoTest ###

def mongoTest (config):
    mongoClient     = MongoClientSingleton (config)
    climateFrontDb  = mongoClient.getDatabase (config.mongoDatabase)
    routeCollection = climateFrontDb.getCollection ("route")

    testRoute = {
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

    res = routeCollection.find ({"origin" : "London"})

    for r in res:
        print (r ['origin'] + " - " + r ['destiny'])

    mongoClient.close ()

### function: opcuaTest ###

def opcuaTest (config):
    climateFrontDb = MongoClientSingleton  (config).getDatabase (config.mongoDatabase)
    serverStock    = ServerOPCUASimulation (config)

    serverStock.startSimulation ()
    serverStock.incrementStock ()

    clientStock = ClientOPCUA (config.serverOPCUASimulationEndpoint)

    varTomatoes = clientStock.getObjectsVar ("2:Stock", "2:Tomatoes")
    varBananas  = clientStock.getObjectsVar ("2:Stock", "2:Bananas")
    varApples   = clientStock.getObjectsVar ("2:Stock", "2:Apples")

    print ("Initial stock tomatoes: " + str (varTomatoes.get_value ()))
    print ("Initial stock bananas: "  + str (varBananas.get_value ()))
    print ("Initial stock apples: "   + str (varApples.get_value ()))

    clientStock.subscribeToVarMongo (varTomatoes, climateFrontDb)
    clientStock.subscribeToVarMongo (varBananas , climateFrontDb)
    clientStock.subscribeToVarMongo (varApples  , climateFrontDb)

    serverStock.incrementStock ()

    print ("Final stock tomatoes: " + str (varTomatoes.get_value ()))
    print ("Final stock bananas: "  + str (varBananas.get_value ()))
    print ("Final stock apples: "   + str (varApples.get_value ()))

########################################################################################################################
#########################                            CLIMATE FRONT                            ##########################
########################################################################################################################

if __name__ == '__main__':
    config = DevelopmentConfig ()

    logging.basicConfig (level = config.logLevel)

    mongoTest (config)
    opcuaTest (config)

    while True:
        time.sleep (100000)