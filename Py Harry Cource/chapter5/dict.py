marks = {
    "Key": "Value",
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92,
    "Eve": 88,
    "List": [1, 2, 3],
    "Tuple": (1, 2, 3),
}

# Functions of dict
print("Items are :", marks.items())  # returns all key-value pairs
print("Keys are :", marks.keys())    # returns all keys
print("Values are :", marks.values())  # returns all values

# Update - add or modify entries
marks.update({"Alice": 95, "Renuka": 100})
print("After update:", marks)

# Get value of a key safely
print("Get Chandu:", marks.get("Chandu"))  # returns None if key not found
# print(marks["Chandu"])  # raises KeyError if key not found
print("Get Alice:", marks.get("Alice"))    # returns 95

# Copy dictionary
marks2 = marks.copy()
print("Second Dictionary:", marks2)

# Pop - remove an item by key
removed_value = marks.pop("Bob")
print(f"Removed Bob's marks: {removed_value}")
print("After pop:", marks)

# Popitem - remove last inserted item
last_item = marks.popitem()
print(f"Removed last item: {last_item}")
print("After popitem:", marks)

# Clear - remove all items
# Uncomment below line if you want to clear the dictionary
marks2.clear()
print("After clear:", marks2)

# Setdefault - get value if key exists else insert the key with given default
result = marks.setdefault("Chandu", 70)
print(f"Setdefault result: {result}")
print("After setdefault:", marks)

# Fromkeys - create a new dict from a sequence of keys
keys = ["Sam", "Tom", "Jerry"]
new_dict = dict.fromkeys(keys, 0)
print("New dictionary using fromkeys:", new_dict)

# Checking membership (in and not in)
print("Is 'Alice' a key in marks?", 'Alice' in marks)
print("Is 'Bob' not a key in marks?", 'Bob' not in marks)
