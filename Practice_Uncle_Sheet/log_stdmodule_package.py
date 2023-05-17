Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

import random

import time

import webbrowser as web

for i in range(1,7):
    number = random.randint(0,9)
    time.sleep(1)
    print(number)

    
3
7
9
2
2
2


time.sleep(5)
url = 'http'

url = 'http:www.google.com/'

web.open(url)
True


url = 'https://github.com/bxlldev'


web.open(url)
True




















import webbrowser as web

import time




import pyautogui



import pyautogui as pg


url = 'https://www.google.com'

web.open(url)
True

time.sleep(2)

pr

pg.write('thailand',interval=0.25)
thailand


pg.press('enter')


pg.screenshort('thailand.png')
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    pg.screenshort('thailand.png')
AttributeError: module 'pyautogui' has no attribute 'screenshort'. Did you mean: 'screenshot'?


pg.screenshot('thailand.png')
<PIL.Image.Image image mode=RGB size=1920x1080 at 0x26E667C7C50>







def UsePyautogui():
    url = 'https://www.google.com'
    web.open(url)
    time.sleep(2)
    pg.write('thailand',interval=0.25)
    pg.press('enter')
    pg.screenshot('thailand.png')

    



UsePyautogui()
UsePyautogui()











import math

from random import  randint


radius = randint(1,9)

area = math.pi*radius**2


print(radius)
4

print(area)
50.26548245743669




def testmath():
    radius = randint(1,9)
    area = math.pi*radius**2
    print(radius)
    print(area)

    


testmath()
2
12.566370614359172





>>> def testmath():
...     radius = randint(1,9)
...     area = math.pi*radius**2
...     print("radius: " + radius)
...     print("area: " + area)
... 
...     
>>> 
>>> 
>>> 
>>> testmath()
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    testmath()
  File "<pyshell#125>", line 4, in testmath
    print("radius: " + radius)
TypeError: can only concatenate str (not "int") to str
>>> 
>>> 
>>> 
>>> def testmath():
...     radius = randint(1,9)
...     area = math.pi*radius**2
...     print("radius: " + str(radius))
...     print("area: " + str(area))
... 
...     
>>> 
>>> 
>>> 
>>> testmath()
radius: 6
area: 113.09733552923255
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
