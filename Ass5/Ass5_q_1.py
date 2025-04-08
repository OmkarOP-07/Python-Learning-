# Q1.
# Write a python program which finds the maximum number from num1 to num2 (num2 inclusive)
# based on the following rules.
# 1. Always num1 should be less than num2
# 2. Consider each number from num1 to num2 (num2 inclusive). Populate the number into a list, if the
# below conditions are satisfied
# a. Sum of the digits of the number is a multiple of 3
# b. Number has only two digits
# c. Number is a multiple of 5
# 3. Display the maximum element from the list
# In case of any invalid data or if the list is empty, display -1.

def isValid(num) :
    sum = 0
    numCopy = num
    while num!= 0:
        lastD = num%10
        sum += lastD
        num //= 10

    if numCopy >=10 and numCopy < 100:
        if sum%3== 0 and numCopy%5 == 0:
            return True 
    
    return False


def funct(num1,num2):
    if num1 > num2 :
        print(-1)
        return
    
    list = []  # Empty String 

    for i in range(num1, num2 + 1):  # Iterate from num1 to num2 (inclusive)
        if isValid(i):  
            list.append(i)  

    
    maxNum = max(list)
    if not list :
        print(-1)
    else:
        print(maxNum)
        
num1 = 11
num2 = 99
funct(num1, num2)