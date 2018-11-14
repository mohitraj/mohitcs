utilization_of_device = [10,12,40,30,0,12,0,70,0,23]
band_witdh = 100

for each in utilization_of_device:
	if each==0:
		continue
	kpi = band_witdh/each
	print (each, ":", kpi)