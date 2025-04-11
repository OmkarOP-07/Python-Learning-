# Define custom exception
class WeakPasswordError(Exception):
    def __init__(self):
        super().__init__("Password must be at least 8 characters long and include at least one uppercase letter and one number.")

def set_password(password):
    try:
        if (len(password) < 8 or
            not any(char.isupper() for char in password) or
            not any(char.isdigit() for char in password)):
            raise WeakPasswordError()
        else:
            print("Password set successfully.")
    except WeakPasswordError as e:
        print("Error:", e)

set_password("pass123")       #Weak
set_password("Pass1234")      #Strong
