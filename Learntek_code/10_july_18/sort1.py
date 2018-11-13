list1 = ['192.168.0.112','192.168.0.110','192.168.0.1','192.168.0.12']

list1.sort(key = lambda x:int(x.rsplit(".",1)[1]))
print list1