import datetime

t1 = datetime.time.hour
print(t1)

d = datetime.date(2020,4,6)
print(d.year)

t2 = datetime.date.today()

timedel = datetime.timedelta(hours=2)
print(timedel)

t3 = datetime.datetime.now()
print(t3)

print(t3 - timedel)