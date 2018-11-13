import time
import datetime


delta1 = datetime.timedelta(days=1,seconds=1)



current_date = datetime.datetime.now()

next_day_date = current_date + delta1

print current_date
print next_day_date




date1 =  next_day_date.strftime('%Y-%m-%d %H:%M:%S')




print int(time.mktime(time.strptime(date1, '%Y-%m-%d %H:%M:%S')))

