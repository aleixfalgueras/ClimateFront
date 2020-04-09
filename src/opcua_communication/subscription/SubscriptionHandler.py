import logging

################################################################################
# class: SubscriptionHandler
################################################################################

class SubscriptionHandler () :

    ### function: datachange_notification ###

    def datachange_notification (self, node, val, data) :
        message = "Node:", node, "Value:", val, "Data:", data

        logging.info (message)
        print (message)