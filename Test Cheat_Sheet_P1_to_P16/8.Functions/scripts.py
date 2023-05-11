
# Functions

## Functions are named blocks of code, designed to do one specific job. Information passed to a function is called an "argument, and information received by a fucntion is called a parameter.


## A simple function


def greeting_user():
    print("Hello user !")

greeting_user()




## Passing an argument

def greet_user(username):
    print("Hello " + username + ", How's going ")

greet_user('Ball')
greet_user('Gam')


## Default values for parameters

def make_icecream(topping = 'chocolate chip'):
    print("Hi, Do you want " + topping + " on top an icecream ?")

make_icecream()
make_icecream('jelly')
make_icecream('conflex')
make_icecream('spinkles')


## Returning a value

def add_numbers(x,y):
    return x + y

sum = add_numbers(2,5)
print(sum)


## or


print(add_numbers(3,5))












