Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


def first_function():
    print("Hello My name is Thanachart !")

    
first_function()
Hello My name is Thanachart !



def second_function(name):
    print("Hello My name is " + name)

    
second_function("Thanachart")
Hello My name is Thanachart

second_function("Pornkamol")
Hello My name is Pornkamol



def third_function(name,age):
    print("Hello My name is " + name)
    print("I am " + str(age) " years old")
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?


def third_function(name,age):
    print("Hello My name is " + name)
    print("I am " + str(age) + " years old")

    
third_function("Thanachart",23)
Hello My name is Thanachart
I am 23 years old






def fourth_function(name,age):
    print("Hello My name is " + name)
    print("I am " + str(age) + " years old")

    

fourth_function(name="Thanachart", age=23)
Hello My name is Thanachart
I am 23 years old




fourth_function(age=23, name="Thanachart")
Hello My name is Thanachart
I am 23 years old



def fifth_function(name,age=23):
    print("Hello My name is " + name)
    print("I am " + str(age) + " years old")

    
fifth_function("Thanachart")
Hello My name is Thanachart
I am 23 years old



fifth_function("Thanachart",50)
Hello My name is Thanachart
I am 50 years old



def sixth_function(name,age=None):
    print("Hello My name is " + name)
    if age:
        print("I am " + str(age) + " years old")

        
sixth_function("Thanachart")
Hello My name is Thanachart

sixth_function("Thanachart",23)
Hello My name is Thanachart
I am 23 years old







def first2_function():
    return "Hello My name is Thanachart !"
... 
>>> hello = first2_function()
>>> 
>>> print(hello)
Hello My name is Thanachart !
>>> 
>>> 
>>> first2_function()
'Hello My name is Thanachart !'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
d
>>> 
>>> 
>>> 
>>> d
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def second2_function(name):
...     return "Hello My name is " + name
... 
>>> 
>>> hello = second2_function("Thanachart")
>>> 
>>> 
>>> print(hello)
Hello My name is Thanachart
>>> 
>>> 
>>> 
>>> 
>>> 
