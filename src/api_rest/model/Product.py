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
        return "Product (id: " + self.id + ", name: " + self.name + ", quantity: " + self.quantity + ")"

    ### function: toJson ###

    def toJson (self):
        return {"id" : self.id, "name" : self.name, "quantity" : self.quantity}