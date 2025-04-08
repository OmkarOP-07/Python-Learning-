# Q3.
# ARS Gems Store sells different varieties of gems to its customers.
# Write a Python program to calculate the bill amount to be paid by a customer based on the list of
# gems and quantity purchased. Any purchase with a total bill amount above Rs.30000 is entitled for 5%
# discount. If any gem required by the customer is not available in the store, then consider total bill
# amount to be -1. ( Calculate the total bill)
# Assume that quantity required by the customer for any gem will always be greater than 0.
# Perform case-sensitive comparison wherever applicable.
# Consider the following Gems. ["Emerald","Ivory","Jasper","Ruby","Garnet"]
# Price in Rs. For each correspondingly: [1760,2119,1599,3920,3999]

def calBillForOneGem(quantity,gem):
    price = -1
    match gem :
        case "Emerald" :
            price = 1760
        case "Ivory" :
            price = 2119
        case "Jaspar" :
            price = 1599
        case "Ruby" :
            price = 3920
        case "Garnet" :
            price = 3999
        case _:
            price = -1 
    if price != -1 :
        return quantity*price
    else :
        return -1 
    
def calBill(gems,quantity):
    totalBill = 0
    for i in range(0, len(gems)):
        if calBillForOneGem(quantity[i],gems[i]) != -1:
            totalBill += calBillForOneGem(quantity[i],gems[i])
        else :
            return -1 
        
    return totalBill

        
        
gems = ["Ivory", "Emerald"]
quantity = [2,3]
print(calBill(gems,quantity))
