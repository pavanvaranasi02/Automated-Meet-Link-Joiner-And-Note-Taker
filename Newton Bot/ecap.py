import webbrowser as web
import pyautogui as p
from pyautogui import click,typewrite,press
from time import sleep


web.open_new_tab("http://www.webprosindia.com/*****/")
sleep(10)
username = "20241A12**"
password = "***********"

click(x=839, y=489,duration=0.5)  # Username Btn
sleep(1)
typewrite(username,interval=0.2)
sleep(1)

click(x=842, y=512,duration=0.5)  # Password Btn
sleep(1)
typewrite(password,interval=0.2)
sleep(1)

press('enter',interval=0.1)
sleep(8)

click(x=131, y=599,duration=0.5) # To click on feedback
sleep(1)

click(x=362, y=523,duration=0.5)   # To operate page we are clicking on some random place.
sleep(1)

press('tab',interval=0.2)
sleep(1)

press('enter',interval=0.1)
sleep(1)

press('down',interval=0.2)
sleep(1)

press('enter',interval=0.1)
sleep(1)

# to press 4 on 150 boxes.

press('tab',interval=0.2)
sleep(1)

for i in range(150):
    typewrite("4")
    sleep(1)
    press('tab')
    sleep(1)

# To press 4 on 8 more boxes which are in the downside.

for i in range(8):
    typewrite("4")
    sleep(1)
    press('tab')
    sleep(1)
  
# To click on submit button.
click(x=773, y=609,duration=0.5)
sleep(2)

