
#for loops

# print ค่า number ในช่วง 10 index แรก 
for number in range(10):
    print(number)


   

# print ค่า number ในช่วง index1 ถึง index11 
for number in range(1,11):
    print(number)





#while loops

#print 'Hello Ball' for a while
while True:
    print('Hello Ball')


#print 'Hello Ball' until get 'break'
while True:
    print('Hello Ball')
    break

#print 'Hello Ball' for a while with "variable"
name = 'Mr.Thanachart'
while name == 'Thanachart':
    print('Hello',name)
    break





#Enumerating iterators (การแจกแจง การลำดับค่า)

names = ['Blue','Red','Green']

for number, name in enumerate(names):
    print(f'{number} is {name}')

for number, name in enumerate(names,5): ## define number = 5 default (start number with '5')
    print(f'{number} is {name}')




#Continue break and else
    
while True:
    name = input('Please enter your name :')
    if name == 'exit':
        break
    elif name == '':
        continue
    else:
        print('Hi '+name)




