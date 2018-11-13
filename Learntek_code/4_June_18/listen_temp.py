from weather import Weather, Unit
import speech_recognition as sr
r = sr.Recognizer()

def listen1():
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        str1 = r.recognize_google(audio)
        return str1
    except Exception as e:
        print e

print "Please tell me the City name, I'll get the Weather Conditions\t"
loc1 = listen1().lower()
print "For ",loc1

weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup_by_location(loc1)
condition = location.condition
print(condition.text)