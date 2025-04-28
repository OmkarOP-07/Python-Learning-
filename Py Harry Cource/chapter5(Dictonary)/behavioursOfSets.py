# ============================
# Concept: Lists inside a Set?
# ============================

# Example 1: Trying to put a list inside a set (this will cause an error)
try:
    s = {1, 2, 3, "set", [1, 2]}  # list [1,2] inside set
except TypeError as e:
    print("Example 1 Error:", e)

# OUTPUT:
# Example 1 Error: unhashable type: 'list'
# Reason: Lists are mutable -> not hashable -> cannot be inside a set.


# Example 2: Using a tuple instead of list inside a set
s = {1, 2, 3, "set", (1, 2)}  # tuple (1,2) is immutable
print("Example 2 Output:", s)

# OUTPUT:
# Example 2 Output: {1, 2, 3, (1, 2), 'set'}
# Reason: Tuples are immutable -> hashable -> can be inside a set.


# Example 3: If you really want a 'list-like' structure inside a set
# Trick: Convert the list to tuple before putting it in the set
lst = [4, 5]
s = {1, 2, 3, tuple(lst)}
print("Example 3 Output:", s)

# Now you cannot change the elements inside the tuple because it's immutable.


# Example 4: What if you want to have a list "around" a set?
# You can have a set of tuples, or a list of lists
list_of_lists = [[1, 2], [3, 4], [5, 6]]
print("Example 4 Output (list of lists):", list_of_lists)

# You can change the list elements here:
list_of_lists[0][0] = 99
print("Modified list_of_lists:", list_of_lists)


# Example 5: Can you have a set of frozensets?
# YES - frozenset is an immutable version of set
fs = frozenset([1, 2])
s = {fs, 3, 4}
print("Example 5 Output (using frozenset):", s)

# You cannot change the frozenset after it is created


# Example 6: Summary

"""
In short:
- List -> mutable -> cannot be inside set
- Tuple -> immutable -> can be inside set
- Frozenset -> immutable set -> can be inside set
- If you need changeable structure -> use list outside of set
"""


# ============================
# EXTRA: Manually simulate a "set of lists"
# ============================

# Store the lists as tuples in the set, and later convert back if needed
set_of_tuples = {(1, 2), (3, 4)}
print("Set of Tuples:", set_of_tuples)

# To modify: remove old tuple, insert a new one
set_of_tuples.remove((1, 2))
set_of_tuples.add((99, 2))
print("Modified Set of Tuples:", set_of_tuples)
