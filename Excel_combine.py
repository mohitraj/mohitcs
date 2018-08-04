import xlwt
import xlrd
import os

wkbk = xlwt.Workbook()
outsheet = wkbk.add_sheet('sheet1')

ch = raw_input( "If header is there press Y or n\t")
sheet_name = raw_input("Enter the sheet name \t")

xlsfiles =  [each for each in  os.listdir(".") if each.endswith("xlsx")]
print "Total files are ", xlsfiles

outrow_idx = 0
for f in xlsfiles:
	print "Processing ",f
	try:
		start_value = 0
		if ch.lower() == 'y':
			start_value = 1
		insheet = xlrd.open_workbook(f).sheet_by_name(sheet_name)
		for row_idx in xrange(start_value,insheet.nrows):
			for col_idx in xrange(insheet.ncols):
				outsheet.write(outrow_idx, col_idx, 
							   insheet.cell_value(row_idx, col_idx))
			outrow_idx += 1
	except Exception as e :
		print e 
	else :
		print "finished ",f
wkbk.save(r'combined.xls')