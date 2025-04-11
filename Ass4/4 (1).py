st = int(input("Starting :"))
end = int(input("Ending :"))

def isArmstring (num) :
    num_str = str(num)
    n = len(num_str)
    sum = 0
    for digit in num_str :
        sum += int(digit)**n
    if sum == num:
        return True
    else:
        return False
    
for i in range(st,end) :
    if(isArmstring(i)) :
        print(i, ",", end = "")