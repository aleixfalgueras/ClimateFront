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
            return self.collection.insert_one (jsonDocument)

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
            return self.collection.update_one (query, newValues)

        except Exception as exc :
            logging.error ("MongoCollectionWrapper: updateOne: update_one failed for the collection '" + self.collectionName + "', query: " +
                   str (query) + ", newValues: " + str (newValues))
            logging.error ("[Exception: " + str (exc) +  "]")


    ### function: updateOneById ###

    def updateOneById (self, id, values) :
        return self.updateOne ({"id": id}, {"$set" : values})

    ### function: updateOneFieldById ###

    def updateOneFieldById (self, id, field, newValue) :
        return self.updateOne ({"id": id}, {"$set" : {field : newValue}})
