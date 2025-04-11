# 9. Problem: Find the maximum number in a list using reduce()
# Statement: Given a list of numbers, find the maximum value.
from functools import reduce

numbers = [1,1,2,3,4,2,4]

max = reduce(lambda a,b : a+b , numbers)
print(max)