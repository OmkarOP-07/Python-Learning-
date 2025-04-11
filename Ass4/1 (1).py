a = int(input("Enter starting number :"))
b = int(input('Enter ending number :'))
c = int(input("Enter step value :"))
toggle_format = input("Enter Toggle format ('h' for horizontal 'v' for vertical) :")


for i in range(a,b+1,c):
    for j in range(1,11,1):
        if toggle_format == "v":
            print(i*j)
        else :
            print(i*j, " ", end = "")
    print("")
