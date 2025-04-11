
class InvalidAgeException(Exception):
    def __init__(self, age):
        super().__init__(f"Registration failed: Age {age} is below the minimum required age of 18.")

def register_voter(age):
    try:
        if age < 18:
            raise InvalidAgeException(age)
        else:
            print("Registration is successful.")
    except InvalidAgeException as e:
        print("Error:", e)

register_voter(20)  # Valid
register_voter(16)  # Invalid
