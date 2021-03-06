import logging

from opcua import Client

from src.opcua_communication.subscription.SubscriptionHandler import SubscriptionHandler
from src.opcua_communication.subscription.SubscriptionMongoCollectionHandler import SubscriptionMongoCollectionHandler


################################################################################
# class: ClientOPCUA
################################################################################

class ClientOPCUA :

    ### function: __init__ ###

    def __init__ (self, urlServer) :
        try :
            self.client = Client (urlServer)

            self.client.connect ()

        except Exception as exc :
            logging.error ("ClientOPCUA: __init__: Error initializing class. URL Server: " + urlServer)
            logging.error ("[Exception: " + str (exc) + "]")


    ### function: getObjectsVar ###

    def getObjectsVar (self, nodeName, varName) :
        try :
            return self.client.get_root_node ().get_child (["0:Objects", nodeName, varName])

        except Exception as exc :
            logging.error ("ClientOPCUA: getObjectsVar: Error getting variable " + varName + " from " + nodeName + " in node '0:Objects'")
            logging.error ("[Exception: " + str (exc) +  "]")


    ### function: subscribeToVar ###

    def subscribeToVar (self, var) :
        try :
            sub = self.client.create_subscription (500, SubscriptionHandler ())

            return sub.subscribe_data_change (var)

        except Exception as exc :
            logging.error ("ClientOPCUA: subscribeToVar: Subscription failed for the var:  " + str(var))
            logging.error ("[Exception: " + str (exc) +  "]")


    ### function: subscribeVarToMongoCollection ###

    def subscribeVarToMongoCollection (self, var, collectionWrapper) :
        try :
            sub = self.client.create_subscription (500, SubscriptionMongoCollectionHandler (collectionWrapper))

            return sub.subscribe_data_change (var)

        except Exception as exc :
            logging.error ("ClientOPCUA: subscribeVarToMongoCollection: Subscription to mongo collection '" +
                           collectionWrapper.collectionName + "' failed for the var:  " + str (var))
            logging.error ("[Exception: " + str (exc) +  "]")