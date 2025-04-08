# "python is a good programming language” --> "Python Is A Good Programming Language”"

def upper(char):
    return (chr(ord(char)-32))

def titleOverride(str):
    if not str :
        return "--Given string is empty--"
    
    newStr = ""
    for i in range(0,len(str)):
        if str[i-1] == " " or i == 0:
            newStr += upper(str[i])
        else :
            newStr += str[i]
            
    return newStr


str = "python is a good programming language"

print(titleOverride(str))