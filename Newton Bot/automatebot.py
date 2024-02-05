import pyttsx3
import psutil
import webbrowser as web
from time import sleep
from datetime import datetime
from pyautogui import click
from pyautogui import press
from pyautogui import hotkey
import pyautogui as p
import schedule
import time


engine = pyttsx3.init('sapi5')
engine.setProperty('rate',150)

def speak(text):
    engine.say(text)
    print(text)
    engine.runAndWait()

def check_battery():
    battery =psutil.sensors_battery()
    p = battery.percent   
    if p>=75:
        speak("Battery is enough for three hours to go")
    elif p<=75 and p>=40:
        speak(f"we have {p} percent so please charge")
    else:
        speak("you need to charge your laptop immidetely")

timetable = {
    "Mon": [
            "Probability and Statistics",
            "Digital Logic and Design",
            "Java Programming",
            "Value Etics and Gender Culture"
            ],
    "Tue": [
            "Probability and Statistics",
            "Digital Logic and Design",
            "Java Programming",
            "Value Etics and Gender Culture"
            ],
    "Wed": [
            "Probability and Statistics",
            "Digital Logic and Design",
            "Digital Electronics Lab"
            ],
    "Thu": [
            "Database Management Systems",
            "Discrete Mathematics",
            "Database Management Systems Lab"
            ],
    "Fri": [
            "Database Management Systems",
            "Discrete Mathematics",
            "Java Programming"
            ],
    "Sat": [
            "Database Management Systems",
            "Discrete Mathematics",
            "Java Programming Lab"
            ],
    "Sun": []
}
day = datetime.now().strftime("%a")   # Returns day in three words.
classes = [x for x in timetable[day]]
totalclassesattended = 0
lastclassleaved = False

def toclickjoinfinally():
    speak("Searching for join button to proceed.")
    p.dragTo(x=1219, y=122,duration=0.3)
    sleep(1)
    joinbtn = p.locateCenterOnScreen("Joinbtn.png")
    sleep(1)
    while joinbtn is None:
        joinbtn = p.locateCenterOnScreen("Joinbtn.png")
        sleep(1)
    speak("join button found.")
    sleep(1)
    hotkey("ctrl","e")
    sleep(1)
    hotkey("ctrl","d")
    sleep(2)
    click(joinbtn)
    sleep(5)

def attendClasses(classes= classes):
    global totalclassesattended
    web.open_new_tab("https://griet.newtonclassroom.com/")
    sleep(8)
    click(x=632, y=554,duration=0.3)
    sleep(2)
    press("pagedown")
    sleep(2)
    speak(f"get ready with your {classes[totalclassesattended]} books.")
    sleep(1)
    click(x=1049, y=203,duration=0.3)
    sleep(2)
    btn = p.locateCenterOnScreen("g_meet.png")
    sleep(1)
    while btn is None:
        btn = p.locateCenterOnScreen("g_meet.png")
        sleep(1)
    click(btn)
    sleep(6)
    toclickjoinfinally()
    speak("Class joined successfully.")
    totalclassesattended += 1

def printOnGoingClass(classes = classes):
    print()
    global totalclassesattended
    print(classes[totalclassesattended-1])

def leave_class():
    print()
    global classes
    global totalclassesattended
    speak("Searching for leave button")
    sleep(1)
    leavebtn = p.locateCenterOnScreen("leavebtn.png")
    sleep(1)
    checked = 0
    while leavebtn is None:
        checked += 1
        if(checked == 5):
            break
        leavebtn = p.locateCenterOnScreen("leavebtn.png")
        sleep(1)
    if(leavebtn is None):
        speak("Ahh I found no class at all.")
    else:
        click(leavebtn)
        sleep(1)
        speak("Leaved class.")
        sleep(1)
        p.hotkey("ctrl", "w")
        sleep(1)
        p.hotkey("ctrl", "w")
        sleep(1)
    if totalclassesattended == len(classes):
        lastclassleaved = True

def timer():
    import time
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    print(f"The Time is: {current_time}", end='\r')

timer()

query = p.prompt(text='Did you start the meet are should i need to: ',title='Verification',default='no')
query = query.lower()

# Monday Schedule

schedule.every().monday.at("08:55").do(attendClasses,classes)
schedule.every().monday.at("09:00").do(printOnGoingClass,classes)
schedule.every().monday.at("10:00").do(leave_class)

schedule.every().monday.at("10:05").do(attendClasses,classes)
schedule.every().monday.at("10:10").do(printOnGoingClass,classes)
schedule.every().monday.at("11:10").do(leave_class)

schedule.every().monday.at("11:15").do(attendClasses,classes)
schedule.every().monday.at("11:20").do(printOnGoingClass,classes)
schedule.every().monday.at("12:20").do(leave_class)

schedule.every().monday.at("13:15").do(attendClasses,classes)
schedule.every().monday.at("13:20").do(printOnGoingClass,classes)
schedule.every().monday.at("14:20").do(leave_class)

# Tuesday Schedule

schedule.every().tuesday.at("08:55").do(attendClasses,classes)
schedule.every().tuesday.at("09:00").do(printOnGoingClass,classes)
schedule.every().tuesday.at("10:00").do(leave_class)


schedule.every().tuesday.at("10:05").do(attendClasses,classes)
schedule.every().tuesday.at("10:10").do(printOnGoingClass,classes)
schedule.every().tuesday.at("11:10").do(leave_class)

schedule.every().tuesday.at("11:15").do(attendClasses,classes)
schedule.every().tuesday.at("11:20").do(printOnGoingClass,classes)
schedule.every().tuesday.at("12:20").do(leave_class)

schedule.every().tuesday.at("13:15").do(attendClasses,classes)
schedule.every().tuesday.at("13:20").do(printOnGoingClass,classes)
schedule.every().tuesday.at("14:20").do(leave_class)

# Wednesday Schedule

schedule.every().wednesday.at("08:55").do(attendClasses,classes)
schedule.every().wednesday.at("09:00").do(printOnGoingClass,classes)
schedule.every().wednesday.at("10:00").do(leave_class)

schedule.every().wednesday.at("10:05").do(attendClasses,classes)
schedule.every().wednesday.at("10:10").do(printOnGoingClass,classes)
schedule.every().wednesday.at("11:10").do(leave_class)

schedule.every().wednesday.at("11:15").do(attendClasses,classes)
schedule.every().wednesday.at("11:20").do(printOnGoingClass,classes)
schedule.every().wednesday.at("12:50").do(leave_class)

# Thursday Schedule

schedule.every().thursday.at("08:55").do(attendClasses,classes)
schedule.every().thursday.at("09:00").do(printOnGoingClass,classes)
schedule.every().thursday.at("10:00").do(leave_class)

schedule.every().thursday.at("10:05").do(attendClasses,classes)
schedule.every().thursday.at("10:10").do(printOnGoingClass,classes)
schedule.every().thursday.at("11:10").do(leave_class)

schedule.every().thursday.at("11:15").do(attendClasses,classes)
schedule.every().thursday.at("11:20").do(printOnGoingClass,classes)
schedule.every().thursday.at("12:50").do(leave_class)

# Friday Schedule

schedule.every().friday.at("08:55").do(attendClasses,classes)
schedule.every().friday.at("09:00").do(printOnGoingClass,classes)
schedule.every().friday.at("10:00").do(leave_class)

schedule.every().friday.at("10:05").do(attendClasses,classes)
schedule.every().friday.at("10:10").do(printOnGoingClass,classes)
schedule.every().friday.at("11:10").do(leave_class)

schedule.every().friday.at("11:15").do(attendClasses,classes)
schedule.every().friday.at("11:20").do(printOnGoingClass,classes)
schedule.every().friday.at("12:50").do(leave_class)

# Saturday Schedule

schedule.every().saturday.at("08:55").do(attendClasses,classes)
schedule.every().saturday.at("09:00").do(printOnGoingClass,classes)
schedule.every().saturday.at("10:00").do(leave_class)

schedule.every().saturday.at("10:05").do(attendClasses,classes)
schedule.every().saturday.at("10:10").do(printOnGoingClass,classes)
schedule.every().saturday.at("11:10").do(leave_class)

schedule.every().saturday.at("11:15").do(attendClasses,classes)
schedule.every().saturday.at("11:20").do(printOnGoingClass,classes)
schedule.every().saturday.at("12:50").do(leave_class)

if 'started' in query or 'yes' in query:
    totalclassesattended += 1
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    if int(current_time[:2]) >= 9 and int(current_time[:2]) < 10:
        print("Going to sleep for 10 mins.")
        sleep(60*10)
    elif int(current_time[:2]) >= 10 and int(current_time[:2]) < 11:
        print("Going to sleep for 10 mins.")
        sleep(60*10)
    elif int(current_time[:2]) >= 11 and int(current_time[:2]) < 12:
        print("Going to sleep for 10 mins.")
        sleep(60*10)
    elif int(current_time[:2]) >= 13 and int(current_time[:2]) < 14:
        print("Going to sleep for 10 mins.")
        sleep(60*10)
    else:
        speak("What class did you start when there are no classes in newton.")
        query1 = p.prompt(text='Enter class name: ',title='checking',default='Joking')
        if 'joking' in query1:
            speak("Try to be honest to me.")
    
elif 'no' in query or 'not' in query:
    import time
    t = time.localtime()
    c_t = time.strftime("%H:%M",t)
    if (int(c_t[0]) >= 9 and int(c_t)<14):
        attendClasses()
    else:
        speak("Everything is under control, Don't worry.")
        totalclassesattended += 1
        printOnGoingClass(classes=classes)

while True:
    schedule.run_pending()
    timer()
    if (totalclassesattended == len(classes)) and lastclassleaved:
        break
    sleep(30)

