#list.sort(cmp=None, key=None, )
import xlrd
import xlsxwriter

def xls_file_read(file_name):

    workbook = xlrd.open_workbook(file_name)
    sheet = workbook.sheet_by_index(0)
    data = [[sheet.cell_value(r,c) for c in xrange(sheet.ncols)] for r in xrange(sheet.nrows)]
    return data
	
list2 = xls_file_read("book1.xlsx")

list3 = [(each[0],each[2]) for each in list2]
print list3
'''
def fun1(a):
	return a[1]
	
	
list2 = xls_file_read("book1.xlsx")

list2.sort(key=fun1)

print list2
'''