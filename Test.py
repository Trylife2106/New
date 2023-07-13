class Flight():
    def __init__(self, seats):
        self.seats = seats
        self.passanger = []

    def add_Person(self, name):
        if self.open_seats() == 0:
            return False
        else:
            self.passanger.append(name)
            return True
    
    def open_seats(self):
        self.ava = self.seats - len(self.passanger)
        print(f"The open Seats are: {self.ava}")
        return self.ava

flight = Flight(3)

people = ["Harry", "Hermione", "Ron", "Draco"]

for person in people:
    if flight.add_Person(person) == True:
        print(f"Added {person} to the flight")
    else:
        print(f"Not Added {person} to the flight because no more open seats")

