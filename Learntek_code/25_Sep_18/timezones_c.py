import pytz

for k,v in pytz.country_names.items():
	if v.lower().startswith("rus"):
		print (k , " : ", v)