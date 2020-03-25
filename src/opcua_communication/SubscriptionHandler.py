import logging

from src.commons import MongoProductFields, MongoCollection


################################################################################
# class: SubscriptionHandler
################################################################################

class SubscriptionHandler () :

    ### function: datachange_notification ###

    def datachange_notification (self, node, val, data) :
        print ("New stock for node:", node, "value:", val, "data:", data)


################################################################################
# class: SubscriptionMongoCollectionHandler
################################################################################

class SubscriptionMongoCollectionHandler () :

    ### function: __init__ ###

    def __init__ (self, mongoDatabase, collection) :
        try:
            self.mongoDatabase  = mongoDatabase
            self.collectionName = collection
            self.collection     = self.mongoDatabase.getCollection (collection)

        except Exception as exc :
            logging.error ("SubscriptionMongoCollectionHandler: __init__: Error initializing class. "
                           "Mongo database: " + mongoDatabase + ", collection: " + collection)
            logging.error ("[Exception: " + str (exc) + "]")

    ### function: datachange_notification ###

    def datachange_notification (self, node, val, data) :
        try:
            if (self.collectionName == MongoCollection.PRODUCT):
                id = str (node) [26 :-2]  # Node(NumericNodeId(ns=2;i=2))

                self.collection.updateOneFieldById (id, MongoProductFields.QUANTITY, str(val))
            else :
                raise Exception ("Unknow collection to subscribe. Collection name: " + self.collectionName)

        except Exception as exc:
            logging.error ("SubscriptionMongoCollectionHandler: datachange_notification: "
                           "Coudn't apply the logic for the collection: " + self.collectionName)
            logging.error ("[Exception: " + str (exc) + "]")
