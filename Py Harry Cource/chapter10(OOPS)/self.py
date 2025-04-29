class Employee :       
    language = "python"    #class attributes
    salary = 1200000
    
    def getInfo(selfObj):
        print(f"The language of employee is {selfObj.language} and salary is {selfObj.salary}")
    '''
    This will give an error coz self is not passed 
    def greet():
    print("Good Morning")
    '''
    # if dont want to use self use @staticmethod
    # it tells the interpreter that this method does not need self object 
    
    @staticmethod 
    def greet():
        print("Good Morning")
        

Tillu = Employee()
Tillu.language = "JavaScript"

Tillu.getInfo()   # it is given as Employye.getInfo(harry) self is given 