#https://github.com/drj11/pypng
#https://github.com/mnooner256/pyqrcode

import pyqrcode  

tup1 = ("Mohit raj","Prem","mahi")

for each in tup1:
	
	qr = pyqrcode.create(each)
	file_name = each+".png"
	qr.png(file_name, scale=6)
	print each
