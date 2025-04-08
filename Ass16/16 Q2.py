class FruitInfo:
    __fruit_name_list = ["Apple", "Guava", "Orange", "Grape", "Sweet Lime"]
    __fruit_price_list = [200, 80, 70, 110, 60]

    def get_fruit_price(fruit_name):
        if fruit_name in FruitInfo.__fruit_name_list:
            i = FruitInfo.__fruit_name_list.index(fruit_name)
            return FruitInfo.__fruit_price_list[i]

    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list

    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list


class Purchase:
    counter = 101

    def __init__(self, customer, fruit_name, quantity):
        self.customer = customer
        self.fruit_name = fruit_name
        self.quantity = quantity
        self.purchase_id = f"P{Purchase.counter}"
        Purchase.counter += 1

    def get_purchase_id(self):
        return self.purchase_id

    def get_customer(self):
        return self.customer

    def calculate_price(self):
        if self.fruit_name in FruitInfo.get_fruit_name_list():
            price = FruitInfo.get_fruit_price(self.fruit_name)
            discount = 0
            if price == max(FruitInfo.get_fruit_price_list()) and self.quantity > 1:
                discount = 2
            elif price == min(FruitInfo.get_fruit_price_list()) and self.quantity >= 5:
                discount = 10
            if self.customer.cust_type.lower() == "wholesale":
                discount += 10

            return price - (price * discount / 100)
        else:
            return -1


class Customer:
    def __init__(self, customer_name, cust_type):
        self.customer_name = customer_name
        self.cust_type = cust_type


c1 = Customer("Anita", "normal")
p01 = Purchase(c1, "Grape", 2)
print(p01.get_customer().customer_name)
print(p01.get_purchase_id())
print(p01.calculate_price())
