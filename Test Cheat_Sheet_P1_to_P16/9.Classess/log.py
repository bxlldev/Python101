Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


class Dog():
    def __init__(self, name):
        self.name = name

        
class Dog():
    def __init__(self, name):
        self.name = name

    
class Dog():
    def __init__(self, name):
        self.name = name
    def sit(self):
        print(self.name + " is sitting !!")

        
my_dog = Dog('Blue terrier')

print(my_dog.name + " is a great dog!")
Blue terrier is a great dog!

my.dog.sit()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    my.dog.sit()
NameError: name 'my' is not defined



my_dog.sit()
Blue terrier is sitting !!




print(my_dog)
<__main__.Dog object at 0x000001928BEBF390>





print(my_dog.name)
Blue terrier



print(my_dog.sit)
<bound method Dog.sit of <__main__.Dog object at 0x000001928BEBF390>>










class SARDog(Dog):
...     def __init__(self.name):
...         
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> class SARDog(Dog):
...     def __init__(self,name):
...         super().__init__(name)
...     def search(self):
...         print(self.name + " is searching.")
... 
...         
>>> 
>>> 
>>> 
>>> 
>>> my_dog = SARDog('Corgi')
>>> 
>>> 
>>> print(my_dog.name + " is a search dog.")
Corgi is a search dog.
>>> 
>>> 
>>> 
>>> 
>>> my_dog.sit()
Corgi is sitting !!
>>> 
>>> 
>>> 
>>> my_dog.search()
Corgi is searching.
>>> 
>>> 
>>> 
>>> 
>>> print(my_dog)
<__main__.SARDog object at 0x000001928BEBEA50>




print(my_dog.name)
Corgi



