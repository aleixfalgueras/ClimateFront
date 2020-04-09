import logging
import sys

from src import config
from src.commons import MongoCollection, MongoProductFields
from src.mongo_adapter.MongoClientSingleton import MongoClientSingleton
from src.opcua_communication.ClientOPCUA import ClientOPCUA
from src.opcua_communication.ServerOPCUASimulation import ServerOPCUASimulation


### function: info ###

def info ():
    print ('\033[1m' + '\033[94m' + "\nCLIMATE FRONT\n")
    print ('\033[94m' + "Actions:\n")
    print ('\033[94m' + "1: Show stock")
    print ('\033[94m' + "2: Reset stock")
    print ('\033[94m' + "3: New stock input")
    print ('\033[94m' + "4: Stop server")


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

    resetStock (productCollection, False)

    # remove old routes and plans

    MongoClientSingleton ().getCollection (MongoCollection.ROUTE).collection.delete_many ({})
    MongoClientSingleton ().getCollection (MongoCollection.PLAN).collection.delete_many ({})

    return server, client


### function: showStock ###

def showStock (productCollection):
    print ("Current stock is: \n")

    tomatoesQuantity = productCollection.find ({MongoProductFields.ID : "2"}) [0] [MongoProductFields.QUANTITY]
    bananasQuantity = productCollection.find ({MongoProductFields.ID : "3"}) [0] [MongoProductFields.QUANTITY]
    applesQuantity = productCollection.find ({MongoProductFields.ID : "4"}) [0] [MongoProductFields.QUANTITY]

    print ("Tomatoes: " + str (tomatoesQuantity))
    print ("Bananas: " + str (bananasQuantity))
    print ("Apples: " + str (applesQuantity))


### function: resetStock ###

def resetStock (productCollection, printMessage = True):
    productCollection.updateOneFieldById ("2", MongoProductFields.QUANTITY, str (0))
    productCollection.updateOneFieldById ("3", MongoProductFields.QUANTITY, str (0))
    productCollection.updateOneFieldById ("4", MongoProductFields.QUANTITY, str (0))

    if (printMessage) : print ("Server stock reset!\n")


### function: incrementStock ###

def newInput (server):
    server.incrementRandomStock ()
    print ("New input processed successfully.\n")


### function: stopServer ###

def stopServer (server):
    server.stopServer ()
    print ("Server stop successfully.")
    print ("Bye!")
    sys.exit (0)

########################################################################################################################
#######################                            DEMO  CLIMATEFRONT                           ########################
########################################################################################################################

logging.basicConfig (level = config.DEMO_OPCUA_LOG_LEVEL)

productCollection = MongoClientSingleton ().getCollection (MongoCollection.PRODUCT)

server, client = startDemo ()

info ()

running = True

while running:
    actionCode = input ('\033[92m' + "\nTell me what to do!\n" + '\033[0m')

    if   actionCode == "1"    : showStock (productCollection)
    elif actionCode == "2"    : resetStock (productCollection)
    elif actionCode == "3"    : newInput (server)
    elif actionCode == "4"    : stopServer (server)
    elif actionCode == "help" : info ()
    else:
        print ("Sorry I don't know the action code: '" + actionCode + "'. Type 'help' for more information.")