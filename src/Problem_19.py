from datetime import date, timedelta
start = date(1901, 01,01)
sunday=0 
while start <= date(2000, 12,31):
    if start.weekday() == 6:
        if start.strftime('%d') == '01':
            sunday=sunday+1
        start = start + timedelta(weeks=1)
    else:
        start = start + timedelta(days=1) 
print sunday 