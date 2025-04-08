print("64. Find max length of consecutive zeros (binary).")


def findConsecZero(str):
    list1 = str.split("1")
    max_count = 0
    for i in list1:
        if max_count < i.count("0"):
            max_count = i.count("0")
    print(max_count)


findConsecZero("0000000000000000001000001000100")