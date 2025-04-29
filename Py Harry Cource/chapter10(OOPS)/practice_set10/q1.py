class Programmer :
    Name = ""
    EmployeeID = None
    Language = None
    
    def __init__(self, Name, EmployeeID, Language):
        self.Name = Name
        self.EmployeeID = EmployeeID
        self.Language = Language
        
    def printInfo(self):
        print("Name :",self.Name)
        print("EmployeeID :",self.EmployeeID)
        print("Language :",self.Language)
        
Programmer1 = Programmer("Chintu",12345678, "Flutter")
Programmer1.printInfo()