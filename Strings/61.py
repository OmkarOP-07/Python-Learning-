print("61. Remove duplicate characters in string.")
str = "banana"
seen = ""
for i in str:
    if i not in seen:
        seen += i
print(seen)