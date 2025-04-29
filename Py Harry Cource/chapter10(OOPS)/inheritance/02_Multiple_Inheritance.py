class Father:
    def father_characteristic(self):
        print("Larger Height")

class Mother:
    def mother_characteristic(self):
        print("Sweet voice")

class Child(Father, Mother):
    def child_characteristic(self):
        print("Child's characteristic: Sweet voice and Larger Height")

c1 = Child()
c1.father_characteristic()
c1.mother_characteristic()
c1.child_characteristic()
