import datetime
time1 = datetime.datetime.now()
time2 = datetime.timedelta(days=3)
time3=time1+time2
print(time3.date())
