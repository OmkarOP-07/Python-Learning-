# 2.Problem: Square each number in a list using map()
# Statement: Given a list of numbers, return a list where each number is squared.
numbers = [1,2,3,4,5,6]
list_of_squares = list(map(lambda a : a*a, numbers))

print(list_of_squares)