import logging
import sys

from src import config
from src.commons import MongoCollection
from src.mongo_adapter.MongoClientSingleton import MongoClientSingleton
from src.opcua_communication.ClientOPCUA import ClientOPCUA
from src.opcua_communication.ServerOPCUASimulation import ServerOPCUASimulation


### function: startDemo ###

def startDemo ():
    server = ServerOPCUASimulation ()

    server.startSimulation ()

    client = ClientOPCUA (config.SERVER_OPCUA_SIMULATION_ENDPOINT)

    varTomatoes = client.getObjectsVar ("2:Stock", "2:Tomatoes")
    varBananas = client.getObjectsVar ("2:Stock", "2:Bananas")
    varApples = client.getObjectsVar ("2:Stock", "2:Apples")

    productCollection = MongoClientSingleton ().getCollection (MongoCollection.PRODUCT)

    client.subscribeVarToMongoCollection (varTomatoes, productCollection)
    client.subscribeVarToMongoCollection (varBananas, productCollection)
    client.subscribeVarToMongoCollection (varApples, productCollection)

    return server, client

### function: showStock ###

def showStock (client):
    print ("Current server stock is: \n")
    varTomatoes = client.getObjectsVar ("2:Stock", "2:Tomatoes")
    varBananas = client.getObjectsVar ("2:Stock", "2:Bananas")
    varApples = client.getObjectsVar ("2:Stock", "2:Apples")

    print ("Stock tomatoes: " + str (varTomatoes.get_value ()))
    print ("Stock bananas: " + str (varBananas.get_value ()))
    print ("Stock apples: " + str (varApples.get_value ()))

### function: incrementStock ###

def incrementStock (server):
    server.incrementStock ()
    print ("Server stock incremented successfully\n")

### function: stopServer ###

def stopServer (server):
    server.stopServer ()
    print ("Server stop successfully")
    print ("Bye!")
    sys.exit (0)

########################################################################################################################
####################                           DEMO  CLIENT SERVER OPC UA                          #####################
########################################################################################################################

logging.basicConfig (level = config.DEMO_OPCUA_LOG_LEVEL)

server, client = startDemo ()

print ("\nDemo Client - Server OPC UA\n")
print ("1: Show stock")
print ("2: Increment stock")
print ("3: Stop server")

running = True

while running:
    actionCode = input ("\nTell me what to do!\n")

    if   actionCode == "1": showStock (client)
    elif actionCode == "2": incrementStock (server); showStock (client)
    elif actionCode == "3": stopServer (server)
    else:
        print ("Sorry I don't know the action code: " + actionCode + "")