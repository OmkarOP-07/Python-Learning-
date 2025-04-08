#Remove Vowels from string 
# “My name is Vivek Pande” --> “My nm s Vvk Pnd”

def funct(str) :
    newStr = ""
    for i in str :
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or  i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' :
            continue
        else :
            newStr += i
            
    return newStr

str = "My name is Vivek Pande"
print(funct(str))
    