
class InvalidMarksError(Exception):
    def __init__(self, marks):
        super().__init__(f"Invalid marks: {marks}. Marks should be between 0 and 100.")

def enter_marks(marks):
    try:
        if not (0 <= marks <= 100):
            raise InvalidMarksError(marks)
        else:
            print(f"Marks entered successfully: {marks}")
    except InvalidMarksError as e:
        print("Error:", e)

enter_marks(85)     # Valid marks
enter_marks(110)    # Invalid

