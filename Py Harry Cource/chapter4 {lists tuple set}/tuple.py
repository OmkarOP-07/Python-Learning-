# tuples are immutable cannot be changed 

a = (2,3,4,2,2,2,5)
print(a.count(2))
print(a)
print(type(a))

sliced = a[1:3]
print(sliced)