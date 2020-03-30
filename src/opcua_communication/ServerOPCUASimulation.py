import logging
from random import randrange

from opcua import Server

from src import config


################################################################################
# class: ServerOPCUASimulation
################################################################################

class ServerOPCUASimulation :

    ### function: __init__ ###

    def __init__ (self) :
        try :
            server = Server ()

            server.set_endpoint (config.serverOPCUASimulationEndpoint)

            server.set_security_IDs ([config.serverOPCUASimulationSecurityIds])
            server.set_security_policy ([config.serverOPCUASimulationSecurityPolicy])

            self.server = server
            self.config = config
            self.stockItems = []

        except Exception as exc:
            logging.error ("ServerOPCUASimulation: __init__: Error initializing 'ServerOPCUASimulation'")
            logging.error ("[Exception: " + str (exc) +  "]")


    ### function: startSimulation ###

    def startSimulation (self) :
        try :
            namespaceIndex = self.server.register_namespace ("http://climateFront.tfg.fib.upc")

            objectsNode = self.server.get_objects_node ()

            stock = objectsNode.add_object (namespaceIndex, "Stock")

            stockItems = self.addStock (stock, namespaceIndex)

            self.stockItems = stockItems

            self.server.start ()

        except Exception as exc :
            logging.error ("ServerOPCUASimulation: startSimulation: Error starting simulation")
            logging.error ("[Exception: " + str (exc) + "]")


    ### function: addStock ###

    def addStock (self, stock, namespaceIndex) :
        try :
            stockItems = []

            tomatoes = stock.add_variable (namespaceIndex, "Tomatoes", 0)
            tomatoes.set_writable ()

            stockItems.append (tomatoes)

            bananas = stock.add_variable (namespaceIndex, "Bananas", 0)
            bananas.set_writable ()

            stockItems.append (bananas)

            apples = stock.add_variable (namespaceIndex, "Apples", 0)
            apples.set_writable ()

            stockItems.append (apples)

            return stockItems

        except Exception as exc :
            logging.error ("ServerOPCUASimulation: addStock: Error adding stock to the OPCUA Server Simulation")
            logging.error ("[Exception: " + str (exc) + "]")


    ### function: incrementStock ###

    def incrementStock (self) :
        try :
            for item in self.stockItems :
                quantity = randrange (10)
                newQuantity = item.get_value () + quantity

                item.set_value (newQuantity)

        except Exception as exc :
            logging.error ("ServerOPCUASimulation: incrementStock: Error incrementing stock in OPCUA Server Simulation")
            logging.error ("[Exception: " + str (exc) + "]")