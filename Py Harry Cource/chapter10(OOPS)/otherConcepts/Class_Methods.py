class Parent :
    a = 1
    
    @classmethod
    def show(cls):
        print("value of a is", cls.a)
    
    
p1 = Parent()
p1.a = 90
p1.show()