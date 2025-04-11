import copy


class StudentRecord:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects

    def add_subject(self, subject):
        self.subjects.append(subject)


record = StudentRecord("Alice", ["Math", "Science", "History"])
historical = copy.deepcopy(record)
record.add_subject("Art")
print("Current subjects:", record.subjects)
print("Historical subjects:", historical.subjects)
