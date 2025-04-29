# factorial

def fact(no) :
    if (no == 1 or no == 0):    # base condition 
        return 1
    return no * fact(no-1)

print(fact(5)) 