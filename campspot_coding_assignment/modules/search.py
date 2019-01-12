from datetime import date

class Search:
    def __init__(self, start_date, end_date):
        self.start_date = date.fromisoformat(start_date)
        self.end_date = date.fromisoformat(end_date)

    def print(self):
        print(f"Start Date: {self.start_date}  End Date: {self.end_date}")