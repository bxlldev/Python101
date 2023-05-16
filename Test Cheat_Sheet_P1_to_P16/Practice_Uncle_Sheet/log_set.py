Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


animal = {'cat','dog','snake','tiger','elephant'}


print(animal)
{'elephant', 'snake', 'dog', 'tiger', 'cat'}


animal.add('fish')



print(animal)
{'elephant', 'snake', 'fish', 'dog', 'tiger', 'cat'}


a
animal.update(['owl','bird'])



print(animal)
{'bird', 'elephant', 'snake', 'fish', 'dog', 'tiger', 'owl', 'cat'}


animal.remove('cat')

>>> print(animal)
{'bird', 'elephant', 'snake', 'fish', 'dog', 'tiger', 'owl'}
>>> 
>>> animal.remove(['fish','dog'])
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    animal.remove(['fish','dog'])
TypeError: unhashable type: 'list'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> print(animal)
{'bird', 'elephant', 'snake', 'fish', 'dog', 'tiger', 'owl'}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> animal.discard('dog')
>>> 
>>> 
>>> 
>>> print(animal)
{'bird', 'elephant', 'snake', 'fish', 'tiger', 'owl'}
>>> 
>>> 
>>> 
>>> 
>>> animal.discard(['bird','elephant'])
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    animal.discard(['bird','elephant'])
TypeError: unhashable type: 'list'
>>> 
>>> 
>>> 
>>> 
