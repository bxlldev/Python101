Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> name = imput("What is your name : ")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    name = imput("What is your name : ")
NameError: name 'imput' is not defined. Did you mean: 'input'?
>>> name = input("What is your name : ")
What is your name : Ball
>>> 
>>> print("Hello, " + name + "!")
Hello, Ball!
>>> 
>>> 
>>> def greetting():
...     name2 = input("What is your name : ")
...     print("Hello, " + name + "!")
... 
...     
>>> 
>>> 
>>> greeting()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    greeting()
NameError: name 'greeting' is not defined. Did you mean: 'greetting'?
>>> 
>>> 
>>> greetting()
What is your name : Thanachart
Hello, Ball!
>>> 
>>> 
>>> 
>>> 
>>> def greetting():
...     name2 = input("What is your name : ")
    print("Hello, " + name2 + "!")

    



greetting()
What is your name : Thanachart
Hello, Thanachart!








age = input("How old are you ? :")
How old are you ? :23

age = int(age)



print(age)
23




pi = input("What's the value of pi? :")
What's the value of pi? :
3.141592653589793238462643383279502884197
3.141592653589793



print(pi)


pi = float(pi)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    pi = float(pi)
ValueError: could not convert string to float: ''




pi = input("What's the value of pi? :")
What's the value of pi? :3.1415



pi = float(pi)



print(pi)
3.1415







def you_age():
    age2 = input("How old are you ? :")
    age2 = int(age2)
    print("Your old is " + int(age2))

    





you_age()
How old are you ? :23
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    you_age()
  File "<pyshell#76>", line 4, in you_age
    print("Your old is " + int(age2))
TypeError: can only concatenate str (not "int") to str





def you_age():
    age2 = input("How old are you ? :")
    age2 = str(age2)
    print("Your old is " + str(age2))

    





you_age()
How old are you ? :23
Your old is 23



