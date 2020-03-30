import logging


################################################################################
# class: MongoCollectionWrapper
################################################################################

class MongoCollectionWrapper :

    ### function: __init__ ###

    def __init__ (self, collection, collectionName) :
        try :
            self.collection = collection
            self.collectionName = collectionName

        except Exception as exc :
            logging.error ("MongoCollectionWrapper: __init__: Error initializing class. Collection: " + collectionName)
            logging.error ("[Exception: " + str (exc) + "]")


    ### function: insert ###

    def insertOne (self, jsonDocument) :
        try :
            self.collection.insert_one (jsonDocument)

        except Exception as exc :
            logging.error ("MongoCollectionWrapper: insertOne: insert_one failed for the collection '" + \
                           self.collectionName + "', query: " + str (jsonDocument))
            logging.error ("[Exception: " + str (exc) +  "]")


    ### function: find ###

    def find (self, query) :
        try :
            return self.collection.find (query)

        except Exception as exc :
            logging.error ("MongoCollectionWrapper: find: Find failed for the collection '" + self.collectionName + "', query: " + str (query))
            logging.error ("[Exception: " + str (exc) +  "]")


    ### function: updateOne ###

    def updateOne (self, query, newValues) :
        try :
            self.collection.update_one (query, newValues)

        except Exception as exc :
            logging.error ("MongoCollectionWrapper: updateOne: update_one failed for the collection '" + self.collectionName + "', query: " +
                   str (query) + ", newValues: " + str (newValues))
            logging.error ("[Exception: " + str (exc) +  "]")


    ### function: updateOneFieldById ###

    def updateOneFieldById (self, id, field, newValue) :
        self.updateOne ({"id": id}, {"$set" : {field : newValue}})

