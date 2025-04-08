print("62. Sum digits in string.")
str = "12abc"
digit = ""
for i in str:
    if i.isdigit():
        digit += i
sum = 0
for j in digit:
    sum += int(j)
print(sum)