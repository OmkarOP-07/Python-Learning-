# : Filter even numbers from a list
# Statement: Given a list of integers, filter out only the even numbers using the filter() function and lambda.

#Sol:

numbers = [1,2,3,4,5,6,7,8,9,10]

list_of_evens = list(filter(lambda a : a%2==0, numbers))

print(list_of_evens)