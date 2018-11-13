import datetime
import time
t1 = datetime.timedelta(days=1)
print t1

t2 = datetime.datetime.now()
#print "Current time is ", t2

#t11 = t1.strftime('%Y-%m-%d %H:%M:%S')
t22 = t2.strftime('%Y-%m-%d %H:%M:%S')
t11= t2- t1
print "jk",t11
t11 = t11.strftime('%Y-%m-%d %H:%M:%S')
print "t11",t11
print "t2", t2
print "t22", t22
print t11
#print t22
print "Previous date epoch", int(time.mktime(time.strptime(t11, '%Y-%m-%d %H:%M:%S')))

print int(time.mktime(time.strptime(t22, '%Y-%m-%d %H:%M:%S')))

print time.strptime(t22, '%Y-%m-%d %H:%M:%S')

