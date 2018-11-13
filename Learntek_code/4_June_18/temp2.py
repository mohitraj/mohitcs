from weather import Weather, Unit
weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup_by_location('Frisco')
condition = location.condition
print(condition.text)

forecasts = location.forecast
for forecast in forecasts:
    print "----------------------------"
    print forecast.text
    print forecast.date
    print "MAX Temperature ", forecast.high
    print "MIN Temperature",forecast.low

