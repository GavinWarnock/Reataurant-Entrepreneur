
class Logger:
    def __init__(self, transaction_count, daily_sales):
        self.transaction_count = transaction_count
        self.daily_sales = daily_sales
    
    def log_transaction(self, order, location_number):
        self.transaction_count += 1
        self.daily_sales += order.price
        file = open("log.txt", "a")
        file.write(f"{self.transaction_count}: {order.dish_name} for store {location_number} for a daily total of ${self.daily_sales}\n")
        file.close()

logger = Logger(0,0)