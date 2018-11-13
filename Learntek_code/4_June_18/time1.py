import time
import datetime

t2=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print t2 
print int(time.mktime(time.strptime(t2, '%Y-%m-%d %H:%M:%S')))