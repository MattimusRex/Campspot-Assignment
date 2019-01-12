class Campsite():
    def __init__(self, campsite_id, name):
        self.id = campsite_id
        self.name = name
        self.reservations = []

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def print(self):
        print(f"Campsite ID: {self.id}  Name: {self.name}")
        print("Reservations:")
        for reservation in self.reservations:
            reservation.print()