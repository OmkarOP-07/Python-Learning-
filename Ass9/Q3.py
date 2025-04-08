import copy


class PatientRecord:
    def __init__(self, name, conditions):
        self.name = name
        self.conditions = conditions

    def update(self, condition):
        self.conditions.append(condition)


record = PatientRecord("John Doe", ["Diabetes", "Hypertension"])
oldRecord = copy.deepcopy(record)
record.update("Asthma")
print("Current record:", record.name, record.conditions)
print("Old record:", oldRecord.name, oldRecord.conditions)
