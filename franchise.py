from orderfactory import Orderfactory

class Franchise:
    def __init__(self, location_number):
        self.location_number = location_number
    

    def place_order():
        order = Orderfactory()
        order.create_order(input("What would you like to order?"))

Franchise.place_order()