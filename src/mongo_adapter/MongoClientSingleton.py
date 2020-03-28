import logging

from pymongo import MongoClient

from src import config
from src.mongo_adapter.MongoDatabaseWrapper import MongoDatabaseWrapper


################################################################################
# class: MongoClientSingleton
################################################################################

class MongoClientSingleton:

    ################################################################################
    # class: __MongoClientSingleton
    ################################################################################

    class __MongoClientSingleton:

        ### function: __init__ ###

        def __init__ (self) :
            try:
                self.connection = MongoClient (config.mongoUrl)

            except Exception as exc:
                logging.error ("__MongoClientSingleton: __init__: Error connecting to " + config.mongoUrl)
                logging.error ("[Exception: " + str (exc) +  "]")


        ### function: getDatabase ###

        def getDatabase (self, databaseName) :
            try:
                return MongoDatabaseWrapper (self.connection.get_database (databaseName))

            except Exception as exc:
                logging.error ("__MongoClientSingleton: getDatabase: Error getting database: '" + databaseName + "'")
                logging.error ("[Exception: " + str (exc) +  "]")


        ### function: getCollection ###

        def getCollection (self, collectionName, databaseName = config.mongoDatabase):
            return self.getDatabase (databaseName).getCollection (collectionName)


        ### function: close ###

        def close (self):
            try:
                self.connection.close ()

            except Exception as exc:
                logging.error ("__MongoClientSingleton: Error closing connection")
                logging.error ("[Exception: " + str (exc) +  "]")


    instance = None


    ### function: __new__ ###

    def __new__(cls):
        try :
            if MongoClientSingleton.instance is None :
                MongoClientSingleton.instance = MongoClientSingleton.__MongoClientSingleton ()

            return MongoClientSingleton.instance

        except Exception as exc :
            logging.error ("MongoClientSingleton: __new__: Error creating object '__MongoClientSingleton'")
            logging.error ("[Exception: " + str (exc) + "]")