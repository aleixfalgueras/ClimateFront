import time

from src import config
from src.commons import MongoCollection, MongoRouteFields, MongoProductFields, RouteState
from src.mongo_adapter.MongoClientSingleton import MongoClientSingleton
from src.opcua_communication.ClientOPCUA import ClientOPCUA
from src.opcua_communication.ServerOPCUASimulation import ServerOPCUASimulation


### function: mongoTest ###

def mongoTest ():
    mongoClient     = MongoClientSingleton ()
    climateFrontDb  = mongoClient.getDatabase (config.mongoDatabase)
    routeCollection = mongoClient.getCollection (MongoCollection.ROUTE)

    testRoute = {
        MongoRouteFields.ID : '1',
        MongoRouteFields.STATE : 'PENDING',
        MongoRouteFields.ORIGIN : 'TEST1',
        MongoRouteFields.DESTINY : 'TEST2',
        MongoRouteFields.DEPARTURE : '20190105',
        MongoRouteFields.ARRIVAL : '2019010',
        MongoRouteFields.PRODUCTS :
        [
            {
                MongoProductFields.ID : '2',
                MongoProductFields.NAME : 'tomatoe',
                MongoProductFields.QUANTITY : '5'
            },
            {
                MongoProductFields.ID : '3',
                MongoProductFields.NAME : 'banana',
                MongoProductFields.QUANTITY : '50'
            }
        ]
    }

    routeCollection.insertOne (testRoute)
    routeCollection.updateOneFieldById ('1', MongoRouteFields.STATE, RouteState.CANCELED)

    res = routeCollection.find ({MongoRouteFields.ORIGIN : "TEST1"})

    for r in res:
        originDestiny = "TEST1 - TEST2"
        originDestinyMongo = r [MongoRouteFields.ORIGIN] + " - " + r [MongoRouteFields.DESTINY]

        if (originDestinyMongo == originDestiny): print ("Find OK")
        if (r [MongoRouteFields.STATE] == RouteState.CANCELED): print ("Update OK")



    mongoClient.close ()


### function: opcuaTest ###

def opcuaTest ():
    serverStock = ServerOPCUASimulation ()

    serverStock.startSimulation ()
    serverStock.incrementStock ()

    clientStock = ClientOPCUA (config.serverOPCUASimulationEndpoint)

    varTomatoes = clientStock.getObjectsVar ("2:Stock", "2:Tomatoes")
    varBananas  = clientStock.getObjectsVar ("2:Stock", "2:Bananas")
    varApples   = clientStock.getObjectsVar ("2:Stock", "2:Apples")

    print ("Initial stock tomatoes: " + str (varTomatoes.get_value ()))
    print ("Initial stock bananas: "  + str (varBananas.get_value ()))
    print ("Initial stock apples: "   + str (varApples.get_value ()))

    productCollection = MongoClientSingleton ().getCollection (MongoCollection.PRODUCT)

    clientStock.subscribeVarToMongoCollection (varTomatoes, productCollection)
    clientStock.subscribeVarToMongoCollection (varBananas, productCollection)
    clientStock.subscribeVarToMongoCollection (varApples, productCollection)

    serverStock.incrementStock ()

    print ("After first increment")

    print ("Initial stock tomatoes: " + str (varTomatoes.get_value ()))
    print ("Initial stock bananas: "  + str (varBananas.get_value ()))
    print ("Initial stock apples: "   + str (varApples.get_value ()))

    serverStock.incrementStock ()

    print ("After second increment")

    print ("Final stock tomatoes: " + str (varTomatoes.get_value ()))
    print ("Final stock bananas: "  + str (varBananas.get_value ()))
    print ("Final stock apples: "   + str (varApples.get_value ()))


########################################################################################################################
#########################                            CLIMATE FRONT                            ##########################
########################################################################################################################

if __name__ == '__main__':

    #mongoTest ()
    opcuaTest ()

    while True:
        time.sleep (100000)
