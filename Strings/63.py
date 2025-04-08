print("63. Remove leading zeros in IP address.")
def removeLeadingZeros(IPstr=""):
    temp = IPstr.split(".")
    list1 = []
    for i in temp:
        list1.append(str(int(i)))
    result = ".".join(list1)
    print(result)


removeLeadingZeros("127.01.01.02")
removeLeadingZeros("127.01.00.02")