from pizza import Pizza
from pasta import Pasta
from salad import Salad
class Orderfactory:

    @staticmethod
    def create_order(order):
        if order == "Pizza" or order == "pizza":
            return Pizza()
        elif order == "Pasta" or order == "pasta":
            return Pasta()
        elif order == "Salad" or order == "salad":
            return Salad()