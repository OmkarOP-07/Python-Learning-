# Take the Username and password as an input define the function which will check the entered password


def checkPasswordStrength(str=""):
    Numbers = SpecialChar = Lower = Upper = False
    Length = len(str)
    for i in str:

        if i.isnumeric():
            Numbers = True
        if not i.isalnum():
            SpecialChar = True
        if i.islower():
            Lower = True
        if i.isupper():
            Upper = True

    if Length > 15 and Numbers and SpecialChar and Lower and Upper:
        return "Passwrod is Very Strong"
    elif Length > 11 and Numbers and SpecialChar:
        return "Password is Strong"
    elif Length >= 8 and Numbers:
        return "Password is Normal"
    else:
        return "Password is Weak"


print(checkPasswordStrength(input("Enter your Password & Chek it's strength!: ")))
