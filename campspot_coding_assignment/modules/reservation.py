from datetime import date

class Reservation:
    def __init__(self, campsite_id, start_date, end_date):
        self.campsite_id = campsite_id
        self.start_date = date.fromisoformat(start_date)
        self.end_date = date.fromisoformat(end_date)

    def print(self):
        print(f"Campsite ID: {self.campsite_id}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")