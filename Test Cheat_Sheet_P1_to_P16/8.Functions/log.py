Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> def greeting_user:
...     
SyntaxError: incomplete input
>>> 
>>> 
>>> def greeting_user():
...     print("Hello user !")
... 
...     
>>> 
>>> 
>>> greeting()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    greeting()
NameError: name 'greeting' is not defined
>>> 
>>> 
>>> 
>>> greeting_user()
Hello user !
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def greet_user(username):
...     print("Hello " + username + " How's going ")
... 
...     
>>> greet_user('Ball')
Hello Ball How's going 
>>> 



def greet_user(username):
    print("Hello " + username + ", How's going ")

    



greet_user('Ball')
Hello Ball, How's going 




greet_user('Gam')
Hello Gam, How's going 








def make_icecream(topping = 'chocolate chip'):
    print("Hi, Do you want " + topping "on top an icecream ?")
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?




def make_icecream(topping = 'chocolate chip'):
    print("Hi, Do you want " + topping + "on top an icecream ?")

    




make_icecream()
Hi, Do you want chocolate chipon top an icecream ?






def make_icecream(topping = 'chocolate chip'):
    print("Hi, Do you want " + topping + " on top an icecream ?")

    



make_icecream()
Hi, Do you want chocolate chip on top an icecream ?





make_icecream('jelly')
Hi, Do you want jelly on top an icecream ?






make_icecream('conflex')
Hi, Do you want conflex on top an icecream ?




make_icecream('spinkles')
Hi, Do you want spinkles on top an icecream ?










def add_numbers(x,y):
    return x + y

sum = add_number(2,5)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    sum = add_number(2,5)
NameError: name 'add_number' is not defined. Did you mean: 'add_numbers'?



sum = add_numbers(2,5)




print(sum)
7






print(add_numbers(3,5))
8





