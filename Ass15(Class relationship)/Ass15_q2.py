class Ticket: counter = 0

def __init__(self, passenger_name, source, destination):
    self.passenger_name = passenger_name
    self.source = source
    self.destination = destination
    self.ticket_id = None

def validate_source_destination(self):
    valid_sources = ["Delhi"]
    valid_destinations = ["Mumbai", "Chennai", "Pune", "Kolkata"]
    return self.source.capitalize() in valid_sources and self.destination.capitalize() in valid_destinations

def generate_ticket(self):
    if self.validate_source_destination():
        Ticket.counter += 1
        self.ticket_id = f"{self.source[0].upper()}{self.destination[0].upper()}{Ticket.counter:02d}"
    else:
        self.ticket_id = None

def get_ticket_id(self):
    return self.ticket_id

def get_passenger_name(self):
    return self.passenger_name

def get_source(self):
    return self.source

def get_destination(self):
    return self.destination

ticket1 = Ticket("Alice", "Delhi", "Mumbai") 
ticket1.generate_ticket() 
print(f"Ticket ID: {ticket1.get_ticket_id()}, Passenger: {ticket1.get_passenger_name()}, Source: {ticket1.get_source()}, Destination: {ticket1.get_destination()}")

ticket2 = Ticket("Bob", "Delhi", "Pune") 
ticket2.generate_ticket() 
print(f"Ticket ID: {ticket2.get_ticket_id()}, Passenger: {ticket2.get_passenger_name()}, Source: {ticket2.get_source()}, Destination: {ticket2.get_destination()}")