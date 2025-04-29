class Calculator :
    
    def __init__(self, x):
        self.x = x
        
    def square(self):
        print(f"square is {self.x * self.x}")
        
    def squareroot(self):
        print(f"square root is {self.x**1/2}")
        
    def cube(self):
        print(f"cube is {self.x * self.x * self.x}")
    
    def findAll(self):
        self.square()
        self.squareroot()
        self.cube()
    
obj1 = Calculator(5)
obj1.findAll()
