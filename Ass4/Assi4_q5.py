a = int(input("Enter starting no: "))
b = int(input("Enter ending no: "))
s = 0

def calFact(num):
    ans = 1
    for i in range(1, num+1):
        ans = ans*i
    return ans


for i in range(a, b+1,1 ):
    c = calFact(i)
    print("Factorial of",i,"is",c)
    s += c

print("Total sum is :", s)