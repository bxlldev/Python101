

#Modules

#Python Standard Library

import random
import time
import webbrowser as web

#ตัวอย่างการใช้งาน Standard Library random, time, and webbrowser


#Utilization of "random" and "time" 
for i in range(1,7):
    number = random.randint(0,9)
    time.sleep(1)
    print(number)

#Utilization of "webbrowser" and "time" 
time.sleep(5)
url = 'https://github.com/bxlldev'

web.open(url)


##################################################################

#Python package

#pip install pyautogui
#ตัวอย่างการใช้งาน pyautogui

import webbrowser as web
import time
import pyautogui as pg

def UsePyautogui():
    url = 'https://www.google.com'
    web.open(url)
    time.sleep(2)
    pg.write('thailand',interval=0.25)
    pg.press('enter')
    pg.screenshot('thailand.png')

UsePyautogui()


##################################################################

#Module

import math
from random import  randint

def testmath():
    radius = randint(1,9)
    area = math.pi*radius**2
    print("radius: " + str(radius))
    print("area: " + str(area))

testmath()




















