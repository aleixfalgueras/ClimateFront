################################################################################
# class: SubscriptionHandler
################################################################################

class SubscriptionHandler () :

    ### function: datachange_notification ###

    def datachange_notification (self, node, val, data) :
        print ("Node:", node, "Value:", val, "Data:", data)
