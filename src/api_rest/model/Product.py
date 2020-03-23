from src.commons import MongoProductFields

################################################################################
# class: Product
################################################################################

class Product ():

    ### function: __init__ ###

    def __init__ (self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity

    ### function: __str__ ###

    def __str__ (self) :
        return "Product (" + MongoProductFields.ID + ": " + self.id + ", " + \
               MongoProductFields.NAME + ": " + self.name + ", " + \
               MongoProductFields.QUANTITY + ": " + self.quantity + ")"

    ### function: toJson ###

    def toJson (self):
        return {
            MongoProductFields.ID : self.id,
            MongoProductFields.NAME : self.name,
            MongoProductFields.QUANTITY : self.quantity
        }


### function: toProduct ###

def toProduct (mongoCursor) :
    products = []

    for product in mongoCursor:
        products.append (Product (
            product [MongoProductFields.ID],
            product [MongoProductFields.NAME],
            product [MongoProductFields.QUANTITY]
        ))

    return products