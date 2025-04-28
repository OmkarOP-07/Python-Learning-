#1 
translator = {
    "Hello": "Namaste",
    "Lion": "Sher",
    "Ajay" : "Dhungun",
    "Naughty": "Badmosh" 
}
# uncomment to see the answer of first question 
# while True :
#    word = input("Enter English Word :")
#    print(translator[word])

#2 
numbers = set()
#uncomment to see the answer of second question 
'''
or i in range(0, 4):
    n = input(f"Enter {i} no :")
    numbers.add(n)

print(f"All unique numbers :{numbers}")
'''

#3 
# comparison operatr == checks for equality between two values
# that's why 20 == 20.0 return true
s1 = set()
s1.add(20)
s1.add(20.0)
s1.add("20")
#uncomment to see the answer of third question 
#print("The set :",s1)

#4 
# It is not a set it is considered as doctonary
s1 = {}
s2 = set() #correct way to declare empty set
#uncomment to see the answer of fourth question 
# print(type(s1), type(s2))

#5 get names and values from user and add in the dictonary 
langDict = {}
for i in range(1, 4 ):
    name = input(f"enter name of {i} person :")
    language = input(f"enter {name}'s fav language :")
    langDict.update({name : language})
    
print(langDict)