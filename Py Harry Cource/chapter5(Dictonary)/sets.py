# Set is unordered and unindexed
# Set does not allow duplicate values
# Set can contain any immutable data type (int, float, string, tuple)
# Set cannot contain mutable data types (list, dict, set)
# You can add or remove items from a set but cannot change the value of an existing item

# Creating a set with integers and a string
set = {80, 81, 82, 83, 84, 85, 80, 82, 81, "84"}
print("Set:", set)  # Duplicates will be automatically removed

# Adding an element to the set
set.add(86)
print("Added 86 in Set:", set)

# Removing an element from the set (raises an error if item not found)
set.remove(80)
print("Removed 80 from Set:", set)

# Discarding an element (does NOT raise an error if item not found)
set.discard(100)  # 100 is not present, but no error will occur
print("Tried discarding 100 (no error if absent):", set)

# Copying a set (shallow copy)
set_copy = set.copy()
print("Copy of the Set:", set_copy)

# Updating the set with multiple elements (can add multiple elements at once)
set.update([87, 88, 89])
print("Updated Set with 87, 88, 89:", set)

# Removing and returning a random item (because sets are unordered)
removed_item = set.pop()
print("Popped (randomly removed) item:", removed_item)
print("Set after popping an item:", set)

# Clearing all elements from the set
set.clear()
print("Cleared Set:", set)

# Some Other Useful Set Operations (on new sets)
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union - combines all unique elements from both sets
print("Union of A and B:", A.union(B))

# Intersection - gets common elements from both sets
print("Intersection of A and B:", A.intersection(B))

# Difference - gets elements present only in the first set
print("Difference of A and B (A - B):", A.difference(B))

# Symmetric Difference - gets elements not common to both sets
print("Symmetric Difference of A and B:", A.symmetric_difference(B))

# Checking Subset and Superset relationships
print("Is A subset of B?", A.issubset(B))
print("Is A superset of B?", A.issuperset(B))
