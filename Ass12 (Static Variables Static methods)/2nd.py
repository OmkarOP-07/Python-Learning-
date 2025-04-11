class Parrot:
    counter = 7001

    def __init__(self, name, color):
        self.__name = name
        self.__color = color
        self.__unique_number = Parrot.counter
        Parrot.counter += 1

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

    def get_unique_number(self):
        return self.__unique_number


parrot1 = Parrot("Coco", "Green")
parrot2 = Parrot("Mango", "Yellow")
parrot3 = Parrot("Ruby", "Red")
parrot4 = Parrot("Sky", "Blue")


parrots = [parrot1, parrot2, parrot3, parrot4]
for parrot in parrots:
    print(f"Name: {parrot.get_name()}, Color: {parrot.get_color()}, Unique Number: {parrot.get_unique_number()}")
