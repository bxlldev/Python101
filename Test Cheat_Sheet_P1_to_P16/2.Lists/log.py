Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
employee = ['somchai', 'sommai', 'somboon']

print(employee)
['somchai', 'sommai', 'somboon']


first_employee = employee[0]




printo(first_employee)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    printo(first_employee)
NameError: name 'printo' is not defined. Did you mean: 'print'?

print(first_employee)
somchai



last_employee = employee[-1]


print(last_employee)
somboon


print(employee[-1])
somboon






for em in employee:
    print(em)

    
somchai
sommai
somboon







s



num = []

for x in range(1,11):
    num.append(x**2)

    
print[num]
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print[num]
TypeError: 'builtin_function_or_method' object is not subscriptable
print[num]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    print[num]
TypeError: 'builtin_function_or_method' object is not subscriptable
print(num)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



for x in range(1,11):
    num.append(x**1)

    

print(num)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num.clear()



print(num)
[]


for x in range(1,11):
    num.append(x**1)

    
print(num)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



num.clear()



for x in range(1,11):
    num.append(x+1)

    


print(num)
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]




num.clear()


print(num)
[]



num = [x**2 for x in range(1,11)]



print(num)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
num.clear()




print(num)
[]





num = [x+2 for x in range(1,11)]



print(num)
[3, 4, 5, 6, 7, 8, 9, 10, 11, 12]



num.clear()



num = [i+2 for i in range(1,11)]



print(num)
[3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
num.clear()





finishers = ['somkiat', 'somchit', 'sompong', 'somyut']


first_two = finishers[:2]



print(first_two)
['somkiat', 'somchit']


last_two = finishers[:-2]



print(last_two)
['somkiat', 'somchit']


last_two = finishers[-1] + finishers[-2]



print(last_two)
somyutsompong


last_two = [finishers[-1] + finishers[-2]]



print(last_two)
['somyutsompong']



last_two = [finishers[-1] +', '+ finishers[-2]]



print(last_two)
['somyut, sompong']



print(finishers[-1] + finishers[-2])
somyutsompong



print(finishers[-1] +', '+ finishers[-2])
somyut, sompong





print(finishers)
['somkiat', 'somchit', 'sompong', 'somyut']





members = ['sumo', 'tekken', 'golf']



copy_of_members = members[:]




print(copy_of_members)
['sumo', 'tekken', 'golf']



print(members)
['sumo', 'tekken', 'golf']



KeyboardInterrupt



number = [x for x in range(1,11)]



print(number)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




number.sort()



print(number)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




number2 = ['19', '2' , '17', '5', '7']



number2.sort()





print(number2)
['17', '19', '2', '5', '7']



number2.sort()



print(number2)
['17', '19', '2', '5', '7']



number2.reverse()



print(number2)
['7', '5', '2', '19', '17']





number2.reverse()


print(number2)
['17', '19', '2', '5', '7']



>>> 
>>> number2.count()
Traceback (most recent call last):
  File "<pyshell#256>", line 1, in <module>
    number2.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> number2.count(2)
0
>>> 
>>> 
>>> number2.count(3)
0
>>> 
>>> 
>>> print(number2)
['17', '19', '2', '5', '7']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 

>>> name2 = ['liony', 'slice', 'bunny', 'alice', 'corp']
>>> 
>>> 
>>> 
>>> 
>>> name2.sort()
>>> 
>>> 
>>> 
>>> print(name2)
['alice', 'bunny', 'corp', 'liony', 'slice']
>>> 
>>> 
>>> 
>>> 
>>> 
