class Customer: 
    def init(self, phone_no, name, age): 
        self.phone_no = phone_no 
        self.name = name 
        self.age = age 
        self.list_of_calls = []

class CallDetail: 
    def init(self, phone_no, called_no, duration): 
        self.phone_no = phone_no 
    self.called_no = called_no 
    self.duration = duration

class Util: list_of_customer_calldetail_objects = []

def parse_customer(self, list_of_customers, list_of_calls):
    for customer in list_of_customers:
        customer.list_of_calls = [call for call in list_of_calls if call.phone_no == customer.phone_no]
        self.list_of_customer_calldetail_objects.append(customer)

cust1 = Customer(9900009901, 'cust1', 23) 
cust2 = Customer(9900009902, 'cust2', 24) 
cust3 = Customer(9900009903, 'cust3', 25) 
list_of_customers = [cust1, cust2, cust3]

call1 = CallDetail(9900009901, 8800123401, 5) 
call2 = CallDetail(9900009903, 8800123402, 10) 

call3 = CallDetail(9900009902, 8800123403, 2)
call4 = CallDetail(9900009901, 8800123404, 8) 
call5 = CallDetail(9900009903, 8800123405, 7) 
call6 = CallDetail(9900009903, 8800123406, 9) 
call7 = CallDetail(9900009901, 8800123407, 4) 
list_of_calls = [call1, call2, call3, call4, call5, call6, call7]

util = Util() 
util.parse_customer(list_of_customers, list_of_calls)

for customer in util.list_of_customer_calldetail_objects: print(f"Customer: {customer.name}, Phone: {customer.phone_no}, Calls:") 
for call in customer.list_of_calls: print(f"    Called: {call.called_no}, Duration: {call.duration} mins")