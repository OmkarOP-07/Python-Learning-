# 10 Problem: Find palindromes in a list using filter()
# Statement: Given a list of words, filter out the palindromes (words that read the same forward and backward).
# from functools import reduce
words = ["non", "kok", "popp","sqaddaqs"]

palindrome = list(filter(lambda a: a == a[::-1], words))

print(palindrome)