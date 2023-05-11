
# Classes

## A class defines the behavior of an object and the kind of information an object can store. The information in a class is stored in attributes, and functions that belong to a class are called methods. A child class inherits the attributes and methods from its parent class.


## Creating a dog class

class Dog():
    def __init__(self, name):
        self.name = name
    def sit(self):
        print(self.name + " is sitting !!")

        
my_dog = Dog('Blue terrier')

print(my_dog.name + " is a great dog!")

my_dog.sit()

print(my_dog.name)



## Inheritance


class SARDog(Dog):
    def __init__(self,name):
        super().__init__(name)
    def search(self):
        print(self.name + " is searching.")



my_dog = SARDog('Corgi')

print(my_dog.name + " is a search dog.")


my_dog.sit()

my_dog.search()


print(my_dog.name)








