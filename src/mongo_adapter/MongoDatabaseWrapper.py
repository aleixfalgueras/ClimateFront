import logging

from src.mongo_adapter.MongoCollectionWrapper import MongoCollectionWrapper


################################################################################
# class: MongoDatabaseWrapper
################################################################################

class MongoDatabaseWrapper:

    ### function: __init__ ###

    def __init__ (self, database):
        try:
            self.database = database

        except Exception as exc :
            logging.error ("MongoDatabaseWrapper: __init__: Error initializing class. Database: " + str (database))
            logging.error ("[Exception: " + str (exc) + "]")


    ### function: getCollection ###

    def getCollection (self, collectionName):
        try:
            return MongoCollectionWrapper (self.database.get_collection (collectionName), collectionName)

        except Exception as exc:
            logging.error ("MongoDatabaseWrapper: getCollection: Error getting collection: '" + collectionName + \
                           "' in database: " + str (self.database))
            logging.error ("[Exception: " + str (exc) +  "]")