# Q1
def fruits():
    fruits = []
    for i in range(1,8):
        x = input(f"Enter {i} fruit name :")
        fruits.append(x)
    
    print(fruits)

# Q2 
def marks():
    marks = []
    for i in range(1,8):
        x = int(input(f"Enter {i} student marks :"))
        marks.append(x)
        
    marks.sort()
    print(marks)

# Q3 

def sumofnums():  
    l = [2,2,3,4]
    print(sum(l))
    

# Q4 
def countzeros():
    l = (1,2,9,0,2,0,2,0)
    x = l.count(0)
    print(x)
    
countzeros()