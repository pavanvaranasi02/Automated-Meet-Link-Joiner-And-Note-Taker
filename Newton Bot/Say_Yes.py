import imp
import speech_recognition as sr
import pyautogui as p
import pyttsx3
import time

engine = pyttsx3.init('sapi5')
engine.setProperty('rate',150)

def speak(text):
    engine.say(text)
    print(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("        ")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,1)
    try:
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said : {query}")

    except:
        return ""
    query = str(query)
    return query.lower()

while True:
    query = listen()

    if 'answer your roll call' in query:
        speak("Be Alert")
    
    elif 'attendence' in query:
        speak("Be Alert")

    elif 'respond to your roll call' in query:
        speak("Be Alert")

    elif 'answer your roll calls' in query:
        speak("Be Alert")

    elif 'respond to your roll calls' in query:
        speak("Be Alert")

    elif 'post your attendence in chat box' in query:
        p.hotkey("ctrl","alt","c")
        time.sleep(1)
        p.typewrite("20241A1256")
        time.sleep(1)
        speak("Task Completed")
        break

    elif '56' in query:
        speak("Present sir")
        speak("Task Completed")
        break

    elif 'roll number 56' in query:
        speak("Present sir")
        speak("Task Completed")
        break

    elif '50' in query:
        while True:
            qr = listen()
            if '6' in qr:
                speak("Present sir")
                speak("Task Completed")
                break
            elif '56' in qr:
                speak("Present sir")
                speak("Task Completed")
                break

    