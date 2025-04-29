class Employee: 
    salary = None
    company = "IRCTC"
    def show(self):
        print(f"The name of the Company is {self.company} and the salary is {self.salary}")


class Programmer(Employee):
    Language = None
    company = "Ishq"
    def showLanguage(self):
         print(f"The name of the Company is {self.company} and the Language is {self.Language}")

a = Employee()
a.salary = 9999
b = Programmer()

b.show()
b.showLanguage()