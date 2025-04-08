#  Problem: Find the sum of squares using map() and reduce()
# Statement: Given a list of numbers, find the sum of their squares.

from functools import reduce

numbers = [1,2,3,4,5]

squares = list(map(lambda a: a*a,numbers))
sum = reduce(lambda a,b : a+b, squares)

print(sum)

# 1,4,9,16,25