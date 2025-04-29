# classes are blueprint to create an object 
class Employee :       
    language = "python"    #class attributes
    salary = 1200000
    
omkar = Employee()
omkar.name = "Omkar"       #object attribute / instance attribute

shubham = Employee()
shubham.name = "Shubham"
shubham.salary = 0

print(omkar.name , omkar.language, omkar.salary)
print(shubham.name , shubham.language, shubham.salary)
print(shubham)

'''
Points to be noted : 
   - Here, name is object attribute and language and salary are class attributes 
'''