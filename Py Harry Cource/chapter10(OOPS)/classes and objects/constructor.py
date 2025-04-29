class Employee :       
    language = "python"    #class attributes
    salary = 1200000
    
    def __init__(self, name, salary, language):   #dunder method which is automatically called 
        print("I am creating an object")
        self.name = name
        self.language = language
        self.salary = salary
        
    def getInfo(selfObj):
        print(f"Language of employee is {selfObj.language} \nSalary is {selfObj.salary}")
        

Tillu = Employee("Tillu", 500000, "Javascript")
Tillu.language = "JavaScript"

Tillu.getInfo()   # it is given as Employye.getInfo(harry) self is given 