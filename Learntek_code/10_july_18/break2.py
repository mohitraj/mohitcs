AV = [1,2,'m',3,"k",4,5,]
product = 0
for each in AV:
	
	if "str" in str(type(each)):  #"<type 'str'>"
		continue
	product = product+each

print "Product is", product