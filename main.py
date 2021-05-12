from datetime import datetime
from meetings.Meeting import Meeting
from meetings.Calendar import Calendar
from json import load, dump

calendar = Calendar()

with open('meetings.json') as file:
    data = load(file)
    for item in data:
        meeting = Meeting(datetime.strptime(item['date'], '%d.%m.%Y %H:%M'), item['title'])
        calendar.add(meeting)

if __name__ == '__main__':
    while True:
        option = input('Co chcesz zrobić? L - lista, D - dodaj, Q - quit: ')
        if option == 'l':
            for _, meeting in calendar.meetings.items():
                print(f'{meeting.date}: {meeting.title}')
        elif option == 'd':
            title = input('Tytuł Spotkania: ')
            date = input('Data spotkania dd.mm.rrrr h:m : ')
            meeting_date = datetime.strptime(date, '%d.%m.%Y %H:%M')
            calendar.add(Meeting(meeting_date, title))

            with open('meetings.json', 'w') as file:
                data = []
                for meeting in calendar.meetings.values():
                    data.append({
                        'title': meeting.title,
                        'date': meeting.date.strftime('%d.%m.%Y %H:%M')
                    })
                dump(data, file)
        elif option == 'q':
            break
        else:
            print('Nie wiem co zrobić..')
