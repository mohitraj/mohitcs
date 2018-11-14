import datetime, pytz
for each in pytz.country_timezones.get("US"):
	#print (pytz.timezone(each))
	print (each.ljust(40," "), datetime.datetime.now(pytz.timezone(each)))