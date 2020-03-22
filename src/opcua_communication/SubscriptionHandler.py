################################################################################
# class: SubscriptionHandler
################################################################################

class SubscriptionHandler () :

    ### function: datachange_notification ###

    def datachange_notification (self, node, val, data) :
        print ("New stock for node:", node, "value:", val, "data:", data)


################################################################################
# class: SubscriptionMongoHandler
################################################################################

class SubscriptionMongoHandler () :

    ### function: __init__ ###

    def __init__ (self, mongoDatabase) :
        self.mongoDatabase = mongoDatabase

    ### function: datachange_notification ###

    def datachange_notification (self, node, val, data) :
        id = str (node) [26 :-2]  # Node(NumericNodeId(ns=2;i=2))

        collection = self.mongoDatabase.getCollection ("product")

        collection.updateOne ({"id" : id}, {"$set" : {"quantity" : str (val)}})