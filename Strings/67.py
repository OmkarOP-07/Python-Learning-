print("67. Remove consecutive duplicates in string.")
from itertools import groupby


def remove_consecutive_duplicates(s):
    return "".join(key for key, _ in groupby(s))



s = "xxxxxyyyyy"
print(f"Original string: {s}")
print("After removing consecutive duplicates:", remove_consecutive_duplicates(s))
