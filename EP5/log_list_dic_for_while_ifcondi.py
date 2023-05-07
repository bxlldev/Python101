Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
friend = ['pig','tiger','snake']

friend.append('turtle')

print
<built-in function print>
print(friend)
['pig', 'tiger', 'snake', 'turtle']

friend.remove('tiger')

print(friend)
['pig', 'snake', 'turtle']


del friend[0]


print(friend)
['snake', 'turtle']



prient(friend[0])
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    prient(friend[0])
NameError: name 'prient' is not defined. Did you mean: 'friend'?
print(friend[0])
snake




print(friend[-1])
turtle



number = [5,7,10,12,2]



number.sort()

print(number)
[2, 5, 7, 10, 12]



del number[0]

del number[-1]


print(number)
[5, 7, 10]



number[0] + number[1] + number[2]
22



print(sum(number))
22




tel = {'ball':'0812345678', 'gam':'0800000000', 'benz':'0811111111'}




print(tel['ball'])
0812345678



print(tel['game'])
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    print(tel['game'])
KeyError: 'game'
print(tel['gam'])
0800000000




print(tel['benz'])
0811111111





tel['ball'] = '0899999999'






print(tel['ball'])
0899999999





print(tel)
{'ball': '0899999999', 'gam': '0800000000', 'benz': '0811111111'}





tel.items()
dict_items([('ball', '0899999999'), ('gam', '0800000000'), ('benz', '0811111111')])



print(friend)
['snake', 'turtle']





for f in friend:
    print(f)

    
snake
turtle




for i in range(5):
    print(i)

    
0
1
2
3
4



list(range(5))
[0, 1, 2, 3, 4]




for i in [0,1,2,3,4]:
    print(i)

    
0
1
2
3
4





print(tel)
{'ball': '0899999999', 'gam': '0800000000', 'benz': '0811111111'}





for t in tel.items():
    print(t)

    
('ball', '0899999999')
('gam', '0800000000')
('benz', '0811111111')





for t in tel.items():
    print(t[1])

    
0899999999
0800000000
0811111111




for t in tel.values():
    print(t)

    
0899999999
0800000000
0811111111



for t in tel.keys():
    print(t)

    
ball
gam
benz




import time



while True:
    print('สวัสดีวันอังคาร')
    time.sleep(1)

    
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
สวัสดีวันอังคาร
Traceback (most recent call last):
  File "<pyshell#171>", line 3, in <module>
    time.sleep(1)
KeyboardInterrupt




while False:
    print('hello')
    print('hello')
    print('hello')
    print('hello')
    print('hello')
    print('hello')
    print('hello')
    print('hello')
    print('hello')

    

friend = 'Tuu'


while friend == 'Tuu':
    print("Let's go")

    
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Let's go
Traceback (most recent call last):
  File "<pyshell#195>", line 2, in <module>
    print("Let's go")
KeyboardInterrupt





def YourMoney(money):
    if money > 300:
        print('กินบุฟเฟ่')

        
def YourMoney(money):
    if money > 300:
        print('กินบุฟเฟ่')
    elif money > 200:
        print('กินข้าวแกง')
    else:
        print('กินเซเว่น')

        


YourMoney(400)
กินบุฟเฟ่



YourMoney(300)
กินข้าวแกง


YourMoney(100)
กินเซเว่น


def YourMoney(money):
    if money >= 300:
        print('กินบุฟเฟ่')
    elif money >= 200:
        print('กินข้าวแกง')
    else:
        print('กินเซเว่น')

        


YourMoney(300)
กินบุฟเฟ่



YourMoney(200)
กินข้าวแกง



YourMoney(100)
กินเซเว่น


True
True


False
False



if True:
    print('hi')

...     
hi
>>> 
>>> 
>>> 
>>> 
>>> 
>>> if False:
...     print('hi')
... 
...     
>>> 
>>> 
>>> 
>>> 
>>> 
>>> money = 100
>>> 
>>> 
>>> while money <= 1000:
...     print('ยอดเงินในบัญชีไม่พอ')
...     time.sleep(1)
... 
...     
ยอดเงินในบัญชีไม่พอ
ยอดเงินในบัญชีไม่พอ
ยอดเงินในบัญชีไม่พอ
ยอดเงินในบัญชีไม่พอ
ยอดเงินในบัญชีไม่พอ
ยอดเงินในบัญชีไม่พอ
ยอดเงินในบัญชีไม่พอ
Traceback (most recent call last):
  File "<pyshell#267>", line 3, in <module>
    time.sleep(1)
KeyboardInterrupt
>>> 
>>> 
>>> 
>>> 
