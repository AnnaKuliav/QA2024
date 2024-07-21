import datetime

start_date = datetime.datetime(2024, 4, 11)
end_date = datetime.datetime(2024, 7, 29)
lecture_number = 1

while start_date <= end_date:
    if start_date.strftime('%a') in ['Mon', 'Thu']:
        print(f'Lecture {lecture_number:2}: {start_date.strftime("%d %b %G")} 19:15')
        lecture_number += 1
    start_date += datetime.timedelta(days=1)


