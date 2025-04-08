class Flower:
    def __init__(self):
        self.flower_name = None
        self.price_per_kg = None
        self.stock_available = None

    def validate_flower(self):
        valid_flowers = {"orchid": 15, "rose": 25, "jasmine": 40}
        return self.flower_name.lower() in valid_flowers

    def validate_stock(self, required_quantity):
        return self.stock_available is not None and required_quantity <= self.stock_available

    def sell_flower(self, required_quantity):
        if self.validate_flower() and self.validate_stock(required_quantity):
            self.stock_available -= required_quantity
            return True
        return False

    def check_level(self):
        order_levels = {"orchid": 15, "rose": 25, "jasmine": 40}
        return self.stock_available < order_levels.get(self.flower_name.lower(), float('inf'))

    def set_flower_name(self, name):
        self.flower_name = name

    def set_price_per_kg(self, price):
        self.price_per_kg = price

    def set_stock_available(self, stock):
        self.stock_available = stock

    def get_flower_name(self):
        return self.flower_name

    def get_price_per_kg(self):
        return self.price_per_kg

    def get_stock_available(self):
        return self.stock_available


flower = Flower()
flower.set_flower_name("Rose")
flower.set_price_per_kg(200)
flower.set_stock_available(30)

print("Valid Flower:", flower.validate_flower())
print("Stock Available:", flower.get_stock_available())

if flower.sell_flower(10):
    print("Flowers sold successfully.")
else:
    print("Sale failed.")

print("Stock after sale:", flower.get_stock_available())
print("Below order level:", flower.check_level())