#if else


name = 'Thanachart'


if name == 'Thanachart':
    print('Hello',name)
else:
    print('You are not Thanachart')



#if elif else

name = input('Please enter your name here :')
#Please enter your name here :Thanachart

if name == 'Thanachart':
    print('Hello Ball')
elif name == 'Pornkamol':
    print('Hello Gam')
else:
    print('Who are you?')



#match-case (เริ่มใช้ใน Python 3.10)

name = input('Please enter your name here:')
#Please enter your name here:Thanachart

match name:
    case 'Thanachart':
        print('Hello Ball')
    case 'Pornkamol':
        print('Hello Gam')
    case _:
        print('Who are you ?')



