class Grandfather:
    def show_grandfather(self):
        print("Grandfather: Harish")

class Father(Grandfather):
    def show_father(self):
        print("Father: Suresh")

class Son(Father):
    def show_son(self):
        print("Son: Raj")

s1 = Son()
s1.show_grandfather()
s1.show_father()
s1.show_son()
