Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> number = (100, 150, 200)
>>> 
>>> 
>>> print(number)
(100, 150, 200)
>>> 
>>> 
>>> 
>>> number.index()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    number.index()
TypeError: index expected at least 1 argument, got 0
>>> number.index(0)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    number.index(0)
ValueError: tuple.index(x): x not in tuple
>>> 
>>> 
>>> 
>>> number.index(100)
0
>>> 
>>> 
>>> number.index(150)
1
>>> 
>>> 
>>> number.index(200)
2
>>> 
>>> 
>>> 
