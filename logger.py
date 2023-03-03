
class Logger:
    def __init__(self):
        self.transaction_count = 0
        self.daily_sales = 0
    
    def log_transaction(self, order, location_number):
        self.transaction_count += 1
        self.daily_sales += order.price
        file = open("log.txt", "a")
        file.write(f"Transaction {self.transaction_count}: {order.dish_name} for store {location_number} for ${order.price} for a daily total of ${self.daily_sales}\n")
        file.close()

logger = Logger()