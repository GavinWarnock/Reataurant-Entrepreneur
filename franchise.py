from orderfactory import Orderfactory
from logger import logger
class Franchise:
    def __init__(self, location_number):
        self.location_number = location_number
    

    def place_order():
        chosen_dish = Orderfactory.create_order(input("What would you like to order? <Pizza, Pasta, or Salad?> "))
        logger.log_transaction(order, location_number)
            
Franchise.place_order()