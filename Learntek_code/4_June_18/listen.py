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
		
print listen1()