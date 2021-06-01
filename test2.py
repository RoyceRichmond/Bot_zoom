from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time
import keyboard
from datetime import datetime

def tabs(a,b):
    for x in range(a):
        keyboard.send("tab", do_press=True, do_release=True)
        time.sleep(b)


link = open("meeting_link.txt","r").read()
account=open("account.txt","r").read()
email,passw=account.split(' ')

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome("chromedriver.exe",options=options)
driver.get(link)
time.sleep(15)


tabs(6,0.3)
keyboard.send("enter", do_press=True, do_release=True)
tabs(2,0.1)
keyboard.send("enter", do_press=True, do_release=True)
time.sleep(5)

for a in email:
	keyboard.write(a)
	time.sleep(0.2)
keyboard.send("tab", do_press=True, do_release=True)

time.sleep(1)
for a in passw:
	keyboard.write(a)
	time.sleep(0.6)
time.sleep(4)

tabs(4,0.3)
keyboard.send("enter", do_press=True, do_release=True)
time.sleep(4)
while True:
    now = datetime.now()
    time.sleep(5)
    tmp=int((now.isoformat()[11:17]).replace(":",""))
    if (tmp>=2326):
        keyboard.send("esc", do_press=True, do_release=True)
        for a in range(2):
            keyboard.send("tab", do_press=True, do_release=True)
            time.sleep(0.3)
        keyboard.send("enter", do_press=True, do_release=True)
        break






