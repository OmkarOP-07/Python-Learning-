# 6. Problem: Find the longest word in a list using reduce()
# Statement: Given a list of words, find the longest word using reduce().

from functools import reduce
list_of_strings = ["omkar", "potdar", "hello", "ksdnskdnk"]
longest = reduce(lambda a,b : a if len(a)>len(b) else b , list_of_strings)

print(longest)
