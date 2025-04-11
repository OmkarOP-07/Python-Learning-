# Q1. Implement the following functions without using inbuild functions, give your functions a unique name.
# 1. capitalize()
# 2. lower()
# 3. upper()
# 4. title()
# 5. islower()
# 6. len()

# 1st 

def myCapitalize(str):
    if len(str) == 0:
        return
    if str[0] >= 'a' and str[0] <= 'z':
        newStr = chr(ord(str[0]) - 32) + str[1:]
    return newStr

def myLower(str):
    if len(str) == 0:
        return
    newStr = ""
    for i in str:
        if i == " ":
            newStr +=" "
        else :
            if i >= 'A' and i <= 'Z':
                newStr += chr(ord(i) + 32)
            else :
                newStr += i
    return newStr

def myUpper(str):
    if len(str) == 0:
        return
    newStr = ""
    for i in str:
        if i == " ":
            newStr +=" "
        else :
            if i >= 'a' and i <= 'z':
                newStr += chr(ord(i) - 32)
            else :
                newStr += i
    return newStr

def myTitle(str):
    if len(str) == 0:
        return
    newStr = ""
    #Make the first letter Uppercase
    if str[0] > 'a' and str[0] <= 'z':
        newStr += chr(ord(str[0]) - 32)

    for i in range(1,len(str)):   
        if str[i-1] == " ":
            if str[i] >= 'a' and str[i] <= 'z':
                newStr += chr(ord(str[i]) - 32)
            else:
                newStr += str[i]
        else :
            if str[i] >= 'A' and str[i] <= 'Z':
                newStr += chr(ord(str[i]) + 32)
            else :
                newStr += str[i]

    return newStr

def myIsLower(str):
    if len(str) == 0:
        return -1
    flag = True
    for i in str :
        if i >= 'A' and i <= 'Z':
            flag = False

    return flag

def myLen(str):
    cnt = 0
    for i in str:
        cnt = cnt+1
    return cnt

str = "helllo omKar or"
print(len(str))
print(myLen(str))