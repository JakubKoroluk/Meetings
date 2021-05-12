from datetime import datetime


class Meeting:
    def __init__(self, date: datetime, title):
        self.title = title
        self.date = date
