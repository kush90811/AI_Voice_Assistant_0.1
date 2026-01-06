import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

with sr.Microphone() as source:
    print("🎤 Say something...")
    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)

        speak("You said " + text)

    except:
        print("Sorry, I could not understand.")
        speak("Sorry, I could not understand")
