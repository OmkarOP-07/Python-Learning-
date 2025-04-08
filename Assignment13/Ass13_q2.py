class CallDetail:
    def __init__(self, phoneno, called_no, duration, call_type):
        self.phoneno = phoneno
        self.called_no = called_no
        self.duration = duration
        self.call_type = call_type

class Util:
    def __init__(self):
        self.list_of_call_objects = []

    def parse_customer(self, list_of_call_string):
        for call in list_of_call_string:
            details = call.split(',')
            call_obj = CallDetail(details[0], details[1], details[2], details[3])
            self.list_of_call_objects.append(call_obj)

    def display_calls(self):
        for call in self.list_of_call_objects:
            print(f"Caller: {call.phoneno}, Called: {call.called_no}, Duration: {call.duration} mins, Type: {call.call_type}")

call1 = '9990000001,9330000001,23,STD'
call2 = '9990000001,9330000002,54,Local'
call3 = '9990000001,9330000003,6,ISD'

list_of_call_string = [call1, call2, call3]

util = Util()
util.parse_customer(list_of_call_string)
util.display_calls()