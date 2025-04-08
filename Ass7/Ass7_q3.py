
import math
from functools import reduce

numbers = [1,2,3,4,5,6]
list_of_product = reduce(lambda a,b : a*b, numbers)
print(list_of_product)