Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

employee = {'John' : 'Man', 'Emily' : 'Woman'}




print(employee)
{'John': 'Man', 'Emily': 'Woman'}



print(employee[John])
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(employee[John])
NameError: name 'John' is not defined

print(employee(John))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(employee(John))
NameError: name 'John' is not defined


print(employee{John})
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('employee'[John])
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print('employee'[John])
NameError: name 'John' is not defined



NameError: name 'John' is not defined
SyntaxError: invalid syntax





print(['color'])
['color']



print(['John'])
['John']



print(employee['John'])
Man






print(employee['Emily'])
Woman






print("What John's gender is" + employee['John'])
What John's gender isMan





print("What John's gender is " + employee['John'])
What John's gender is Man






print("What Emily's gender is " + employee['Emily'])
What Emily's gender is Woman







employee['Jack'] = 'Man'






print(employee)
{'John': 'Man', 'Emily': 'Woman', 'Jack': 'Man'}





employee['Jenny'] = 'Woman'





print(employee)
{'John': 'Man', 'Emily': 'Woman', 'Jack': 'Man', 'Jenny': 'Woman'}








employee.items()
dict_items([('John', 'Man'), ('Emily', 'Woman'), ('Jack', 'Man'), ('Jenny', 'Woman')])






age_employee = {'Eric' : 18, 'Jimmy' : 20, 'Buck' : 17}



for name, age in age_employee.items():
    print(name + ' is ' + str(age) + ' year olds')

    
Eric is 18 year olds
Jimmy is 20 year olds
Buck is 17 year olds







print(age_employee['Eric'])
18



print(age_employee['Jimmy'])
20





print(age_employee['Buck'])
17

>>> 
>>> 
>>> 
>>> 
>>> 
>>> for name in age_employee.keys():
...     print(name + ' is employee')
... 
...     
Eric is employee
Jimmy is employee
Buck is employee
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> for age in age_employee.values():
...     print( str(age) + " is all ages of all employee")
... 
...     
18 is all ages of all employee
20 is all ages of all employee
17 is all ages of all employee
>>> 
>>> 
>>> 
>>> for age in age_employee.values():
...     print( str(age) + " is the ages of some employee")
... 
...     
18 is the ages of some employee
20 is the ages of some employee
17 is the ages of some employee
>>> 
>>> 
>>> 
>>> 
