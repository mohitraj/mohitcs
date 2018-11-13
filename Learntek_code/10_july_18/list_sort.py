list1 = ['192.168.0.1','192.168.0.236','192.168.0.67','192.168.0.5','192.168.0.2' ]


'''
def fun1(ip):
	a = int(ip.rsplit(".",1)[1])
	return a
'''
list1.sort(key = lambda ip: int(ip.rsplit(".",1)[1]))

print list1


