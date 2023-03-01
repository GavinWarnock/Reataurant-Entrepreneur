from pizza import Pizza
from pasta import Pasta
from salad import Salad
class Orderfactory:

    @staticmethod
    def create_order(order):
        if order == "Pizza" or order == "pizza":
            return Pizza("Pizza", 5)
        elif order == "Pasta" or order == "pasta":
            return Pasta("Pasta", 15)
        elif order == "Salad" or order == "salad":
            return Salad("Salad", 10)