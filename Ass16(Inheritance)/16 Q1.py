class Apparel:
    __counter = 100

    def __init__(self, price, item_type):
        Apparel.__counter += 1
        self.__item_id = Apparel.__counter
        self.__price = price
        self.__item_type = item_type

    def get_item_id(self):
        if self.__item_type == "cotton":
            return f"C{self.__item_id}"
        else:
            return f"S{self.__item_id}"

    def get_price(self):
        return self.__price

    def get_item_type(self):
        return self.__item_type

    def calculate_price(self):
        return self.__price + (self.__price * 5 / 100)

    def print_Apparel(self):
        print(
            f"{self.get_item_id()}\nItem id: {self.get_item_type()} \nPrice:{self.calculate_price()}"
        )


class Cotton(Apparel):
    def __init__(self, price, discount):
        super().__init__(price, "cotton")
        self.discount = discount

    def get_discount(self):
        return self.discount

    def calculate_price(self):
        old_price = super().calculate_price()
        discount_price = old_price - (old_price * self.discount / 100)
        final_price = discount_price + (discount_price * 10 / 100)
        return final_price


class Silk(Apparel):

    def __init__(self, price):
        super().__init__(price, "silk")
        self.points = 0

    def calculate_price(self):
        old_price = super().calculate_price()
        if old_price > 10000:
            self.points += 10
        else:
            self.points += 3
        new_price = old_price + (old_price * 10 / 100)
        return new_price

    def get_points(self):
        return self.points

    def print_Apparel(self):
        super().print_Apparel()
        print(f"Points: {self.get_points()}")


c1 = Cotton(700,10)
c1.print_Apparel()

s1 = Silk(10000)
s1.print_Apparel()
