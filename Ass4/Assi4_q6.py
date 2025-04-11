st = int(input("Enter starting no"))
end = int(input("Enter ending no"))

def printUnique(st,end):
    for i in range (st, end + 1):
        num = i
        visited = [0,0,0,0,0,0,0,0,0,0]
        
        while (num):
            if visited[num % 10] == 1:
                break
            visited[num % 10] = 1
            num = (int)(num / 10)
 
        if num == 0:
            print(i, end = " ")


printUnique(st, end)