from src.mongo_adapter.MongoCollectionWrapper import MongoCollectionWrapper
import logging


################################################################################
# class: MongoDatabaseWrapper
################################################################################

class MongoDatabaseWrapper:

    ### function: __init__ ###

    def __init__ (self, database):
        self.database = database

    ### function: getCollection ###

    def getCollection (self, collection):
        try:
            return MongoCollectionWrapper (self.database.get_collection (collection))

        except Exception as exc:
            logging.error ("MongoDatabaseWrapper: getCollection: Error getting collection: '" + collection + "' in database: " + self.database)
            logging.error ("[Exception: " + str (exc) +  "]")