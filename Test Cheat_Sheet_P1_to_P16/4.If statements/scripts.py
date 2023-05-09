# If statements

## If statements are used to test for particular conditions and respond appropriarely


###Conditional Test

equals x == 42
not equal x != 42
greater than x > 42
or equal to x >= 42
less than x < 42
or equal to x <= 42


###Conditional Test with Lists

namelist = ['trek', 'giat', 'dinosaur']

print(namelist)

'trek' in namelist
#True

'small_trek' not in namelist
#True

'trek' not in namelist
#False

'small_trek' in namelist
#False


###Assigning boolean values

game_active = True
can_edit = False


### A simple if test

if age >= 18:
    print("You can vote here!")


### if-elif-else statements

    if age < 4:
        ticket_price = 0
    elif age < 18:
        ticket_price = 10
    else:
        ticket_price = 15











