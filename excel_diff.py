import xlrd

def xls_file_read(file_name):
    workbook = xlrd.open_workbook(file_name)
    sheet = workbook.sheet_by_index(0)
    data = [[sheet.cell_value(r,c) for c in xrange(sheet.ncols)] for r in xrange(sheet.nrows)]
    return data
	
	
file_one = "data1.xlsx"
file_two = "data2.xlsx"

file1_data = xls_file_read(file_one)
file2_data = xls_file_read(file_two)

#print file1_data, file2_data

print "First file - Second file"
for each in file1_data:
	if each not in file2_data:
		print each
		
print "Second file - first file"
for each in file2_data:
	if each not in file1_data:
		print each