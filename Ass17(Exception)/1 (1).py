class OutOfStockError(Exception):
    def __init__(self, item_name):
        super().__init__(f"Sorry, the item '{item_name}' is out of stock.")

def buy_item(item_name, stock):
    try:
        if stock == 0:
            raise OutOfStockError(item_name)
        else:
            print(f"'{item_name}' added to cart successfully.")
    except OutOfStockError as e:
        print(e)
    else:
        print("Thank you for shopping with us.\n")

buy_item("Wireless Mouse", 5)     # In stock
buy_item("Bluetooth Speaker", 0) # Out of stock
