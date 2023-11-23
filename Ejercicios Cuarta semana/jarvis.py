import speech_recognition as sr
import pyttsx3


nombres = []

listener = sr.Recognizer()

engine = pyttsx3.init()


def talk(rec):
    engine.say(rec)
    nombres.append(rec)
    engine.runAndWait()
    


try:
    with sr.Microphone() as source:
        for i in range (2):
            print("Escuchando ",i+1)
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            talk(rec)
except:
    pass


for nombre in nombres:
    print(nombre)