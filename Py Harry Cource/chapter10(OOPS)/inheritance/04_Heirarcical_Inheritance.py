class Teacher:
    def teach(self):
        print("Teaching subject")

class MathsTeacher(Teacher):
    def maths(self):
        print("Teaches Mathematics")

class ScienceTeacher(Teacher):
    def science(self):
        print("Teaches Science")

m1 = MathsTeacher()
s1 = ScienceTeacher()

m1.teach()
m1.maths()

s1.teach()
s1.science()
