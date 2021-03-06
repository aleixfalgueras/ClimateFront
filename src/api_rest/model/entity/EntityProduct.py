from src.api_rest.model.entity.Entity import Entity
from src.commons import MongoProductFields


################################################################################
# class: EntityProduct
################################################################################

class EntityProduct (Entity) :

    ENTITY_NAME = "Product"


    ### function: __init__ ###

    def __init__ (self, id, name, quantity) :
        self.id = id
        self.name = name
        self.quantity = quantity


    ### function: __str__ ###

    def __str__ (self) :
        return "Product (" + MongoProductFields.ID + ": " + self.id + ", " + \
               MongoProductFields.NAME + ": " + self.name + ", " + \
               MongoProductFields.QUANTITY + ": " + self.quantity + ")"


    ### function: toJson ###

    def toJson (self) :
        return {
            MongoProductFields.ID : self.id,
            MongoProductFields.NAME : self.name,
            MongoProductFields.QUANTITY : self.quantity
        }