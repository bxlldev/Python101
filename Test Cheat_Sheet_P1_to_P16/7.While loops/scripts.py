
# While loops

## A while loop repeats a block of code as long as a certain condition is true


### A simple while loop

current_value = 1
while current_value <= 5:
    print(current_value)
    current_value += 1

#### Note: current_value will print out with +1 until within <= 5 it will print out until break the loop

print(current_value)

#### Note: Therefore the last value of "current_value" will be 5+1 = 6




### Letting the user choose when to quit

msg = ''

while msg != 'quit':
    msg = input("What's your message? :")
    print(msg)

### input anything and print until input get 'quit', it will be finish the loop




