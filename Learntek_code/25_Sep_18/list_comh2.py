list_ip = ['192.168.0.222','192.168.0.120','192.168.0.23','192.168.0.20','192.168.0.45']

list2 = [int(each.rsplit(".",1)[1])     for each in list_ip]

print (list2)