a = "Helloooo"
vow="aeiouAEIOU"
print("".join(reversed(a)))

num =a.count("a")
num+=a.count('e')
num+=a.count('i')
num+=a.count('o')
num+=a.count('u')


print("Number of Vowels are ",num)
