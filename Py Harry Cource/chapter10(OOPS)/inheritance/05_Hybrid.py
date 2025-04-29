class Principal:
    def manage(self):
        print("Manages school")

class SeniorTeacher(Principal):
    def senior_teach(self):
        print("Teaches and manages department")

class SportsCoach:
    def coach(self):
        print("Coaches students in sports")

class PEteacher(SeniorTeacher, SportsCoach):
    def pe_teach(self):
        print("Teaches Physical Education")

pt = PEteacher()
pt.manage()
pt.senior_teach()
pt.coach()
pt.pe_teach()
