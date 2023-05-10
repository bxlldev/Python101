
#Dictionaries

## Dictionaries store connections between pieces of infomation, Each item in dictionary is a key-values pair


### A Simple Dictionary

employee = {'John' : 'Man', 'Emily' : 'Woman'}
print(employee['John'])
print(employee['Emily'])

### Accessing a value

print("What John's gender is " + employee['John'])
print("What Emily's gender is " + employee['Emily'])


### Adding a new key-values pair (Adding new items to Dictionary )

employee['Jack'] = 'Man'
employee['Jenny'] = 'Woman'

print(employee)


### Looping through all key-values pairs (with "Key+Value"in for loop)

age_employee = {'Eric' : 18, 'Jimmy' : 20, 'Buck' : 17}

for name, age in age_employee.items():
    print(name + ' is ' + str(age) + ' year olds')



### Looping through all keys (with only "Key" in for loop)


for name in age_employee.keys():
    print(name + ' is employee')

    

### Looping through all the values (with only "Value" in for loop)


for age in age_employee.values():
    print( str(age) + " is the ages of some employee")






