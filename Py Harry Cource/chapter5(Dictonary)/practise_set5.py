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
for i in range(0, 4):
    n = input(f"Enter {i} no :")
    numbers.add(n)
    
print(f"All unique numbers :{numbers}")