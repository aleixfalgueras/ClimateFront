import logging


################################################################################
# class: MongoCollectionWrapper
################################################################################

class MongoCollectionWrapper:

    ### function: __init__ ###

    def __init__ (self, collection):
        self.collection = collection

    ### function: insert ###

    def insertOne (self, query):
        try:
            self.collection.insert_one (query)
        except Exception as exc:
            logging.error ("MongoCollectionWrapper: insertOne: insert_one failed for the collection " + self.collection + ", query: " + query)
            logging.error ("[Exception: " + str (exc) +  "]")

    ### function: find ###

    def find (self, query):
        try:
            return self.collection.find (query)

        except Exception as exc:
            logging.error ("MongoCollectionWrapper: find: Find failed for the collection " + self.collection + ", query: " + query)
            logging.error ("[Exception: " + str (exc) +  "]")

    ### function: updateOne ###

    def updateOne (self, query, newValues):
        try:
            return self.collection.update_one (query, newValues)

        except Exception as exc:
            logging.error ("MongoCollectionWrapper: updateOne: update_one failed for the collection " + self.collection + ", query: " +
                   query + ", newValues: " + newValues)
            logging.error ("[Exception: " + str (exc) +  "]")

    ### function: updateOneFieldById ###

    def updateOneFieldById (self, id, field, newValue):
        return self.updateOne ({"id": id}, {"$set" : {field : newValue}})

