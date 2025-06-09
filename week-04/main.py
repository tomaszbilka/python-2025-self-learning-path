import uuid
from datetime import datetime 

class Entity:
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
    def __repr__(self):
        return f"Entity: {self.id} created at: {self.created_at}, last updated at: {self.updated_at}"
 
class Event(Entity):
    def __init__(self, name, date, location, capacity):
        super().__init__()
        self.name = name
        self.date = date
        self.location = location
        self.capacity = capacity
        self.tickets = []
        
    def add_ticket(self, ticket):
        if len(self.tickets) < self.capacity:
            self.tickets.append(ticket)
            return True
        else:
            raise Exception("Event is fully booked.")
        
    def __len__(self):
        return self.capacity
                
        
class User(Entity):
    active_users = 0
    
    @classmethod
    def active_users_count(cls):
        return cls.active_users
    
    def __init__(self, name):
        super().__init__()
        self.name = name
        User.active_users += 1
        
    def show_user_details(self):
        return f"Name: {self.name}, ID: {self.id}"
    
    def __repr__(self):
        return f"User: {self.name}, ID: {self.id}"
    
class Ticket(Entity):
    def __init__(self,event, price):
        super().__init__()
        self.event = event
        self.price = price
        self.is_reserved = False

    def reserve(self):
        self.is_reserved = True
        
    def show_ticket_details(self):
        raise NotImplementedError("Subclasses must implement this method")
        
class VIPTicket(Ticket):
    def __init__(self, event, price, perks):
        super().__init__(event, price)
        self.perks = perks    
        
    def show_ticket_details(self):
        return f"VIP Ticket: {self.event.name}, Price: {self.price}, Perks: {self.perks}"

class StandardTicket(Ticket):
    def __init__(self, event, price):
        super().__init__(event, price)
        
    def show_ticket_details(self):
        return f"Standard Ticket: {self.event.name}, Price: {self.price}"
        
class Reservation(Entity):
    def __init__(self, user, ticket):
        super().__init__()
        if ticket.is_reserved:
            raise Exception("Ticket already reserved.")
        self.user = user
        self.ticket = ticket
        self.ticket.reserve()

def main():
    event = Event("Python Conf 2025", datetime(2025, 9, 15), "Warszawa", capacity=100)
    user1 = User("Tomasz")
    user2 = User("Jan")
    
    vip_ticket = VIPTicket(event, 300.0, perks=["Premium seat", "Lunch", "Backstage pass"])
    event.add_ticket(vip_ticket)
    standard_ticket = StandardTicket(event, 100.0)
    event.add_ticket(standard_ticket)

    reservation = Reservation(user1, vip_ticket)
    print(vip_ticket.show_ticket_details()) # use polymorphism to show different ticket details
    print(standard_ticket.show_ticket_details()) # use polymorphism to show different ticket details

    print(len(event)) # use __len__ which override len(event)
    print(user2) #show __repr__
    print(f"Active users: {User.active_users_count()}") # use class method
    print(f"{user1.name} reserved a VIP ticket for {event.name}")

if __name__ == "__main__":
    main()
