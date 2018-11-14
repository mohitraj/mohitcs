list_ip = ['192.168.0.222','192.168.0.120','192.168.0.23','192.168.0.20','192.168.0.45']

def fun1(ip):
	return int(ip.rsplit('.',1)[1])



list_ip.sort( key = fun1)
print (list_ip)