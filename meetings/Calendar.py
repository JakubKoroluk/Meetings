from datetime import datetime, timedelta
from meetings.Meeting import Meeting


class Calendar:
    def __init__(self):
        self.meetings = {}

    def is_available(self, date: datetime):
        return date not in self.meetings

    def add(self, meeting: Meeting):
        if self.is_available(meeting.date):
            self.meetings[meeting.date] = meeting

    # def show_all_meetings(self):
    #     for x in self.meetings:
    #         return f'Data spotkania {self.meetings}'

    def next_available_slot(self, date: datetime):
        meeting_date = date
        while not self.is_available(meeting_date):
            meeting_date += timedelta(minutes=60)
        return meeting_date
        # storzenie zmiennej potencjalnej godziny spotkania
        # while - dopoki potencjalna godzina spotkania nie jest wolna
        # dodawaj po jednej godzinie do potencjalnej godziny spotkania
