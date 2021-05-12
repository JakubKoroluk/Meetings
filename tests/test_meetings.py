from datetime import datetime, timedelta
from meetings.Meeting import Meeting
from meetings.Calendar import Calendar


def test_add_meeting():
    # given
    meeting = Meeting(datetime(2020, 5, 2, 12, 0), 'Golf')
    meeting2 = Meeting(datetime(2020, 5, 2, 12, 0), 'Golf')
    calendar = Calendar()
    # when
    calendar.add(meeting)
    calendar.add(meeting2)

    # then
    assert len(calendar.meetings) == 1


def test_check_next():
    # given
    meeting = Meeting(datetime(2020, 5, 2, 12, 0), 'Golf')
    meeting2 = Meeting(datetime(2020, 5, 2, 13, 0), 'Golf')
    calendar = Calendar()
    calendar.add(meeting)
    calendar.add(meeting2)

    # when
    next_time_slot = calendar.next_available_slot(datetime(2020, 5, 2, 12, 0))

    # then
    assert next_time_slot == datetime(2020, 5, 2, 14, 0)
