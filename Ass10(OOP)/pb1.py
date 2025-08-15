#class course
class Course:
    def __init__(self, name, code, instructor):
        self.course_name = name
        self.course_code = code
        self.instructor = instructor
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)

    def show_details(self):
        print(f"\nCourse: {self.course_name} ({self.course_code})")
        print(f"Instructor: {self.instructor}")
        print(f"Enrolled Students: {', '.join(self.students) if self.students else 'None'}")


class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease
        self.treatment = None

    def assign_treatment(self, treatment):
        self.treatment = treatment

    def show_details(self):
        print(f"\nPatient: {self.name}, Age: {self.age}")
        print(f"Disease: {self.disease}")
        print(f"Treatment: {self.treatment if self.treatment else 'Not assigned'}")


class Event:
    def __init__(self, title, date, location):
        self.title = title
        self.date = date
        self.location = location
        self.attendees = []

    def add_attendee(self, person):
        self.attendees.append(person)

    def show_details(self):
        print(f"\nEvent: {self.title} on {self.date} at {self.location}")
        print(f"Attendees: {', '.join(self.attendees) if self.attendees else 'No attendees yet'}")


class Candidate:
    def __init__(self, name, party, state):
        self.name = name
        self.party = party
        self.state = state
        self.votes = 0

    def add_votes(self, count):
        self.votes += count

    def show_details(self):
        print(f"\nCandidate: {self.name} ({self.party}) from {self.state}")
        print(f"Total Votes: {self.votes}")


class Experiment:
    def __init__(self, title, scientist, hypothesis):
        self.title = title
        self.scientist = scientist
        self.hypothesis = hypothesis
        self.results = None

    def record_results(self, results):
        self.results = results

    def show_details(self):
        print(f"\nExperiment: {self.title}")
        print(f"Scientist: {self.scientist}")
        print(f"Hypothesis: {self.hypothesis}")
        print(f"Results: {self.results if self.results else 'Pending'}")
