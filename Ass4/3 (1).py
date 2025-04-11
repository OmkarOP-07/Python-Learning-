st_ind = int(input("Enter starting index :"))
end_ind = int(input("Enter ending index :"))
cnt = 0

for i in range(st_ind,end_ind+1):
    if i%2 == 0 or i%3 == 0 or i%5 == 0 :
        cnt = cnt +1
        print(i," ",end = "")
    
print("(Count :",cnt,")")
    