import pyttsx3

def speak(var):
    speak = pyttsx3.init()
    speak.setProperty('rate',170)
    voices = speak.getProperty('voices')
    speak.setProperty('voice',voices[0].id)
    speak.say(var)
    speak.runAndWait()