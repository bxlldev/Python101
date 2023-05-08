#Lists

## A list stores a series of items in a particular order. You access items using an index, or within a loop.


### Making a list

bikes = ['trek', 'redline', 'giant']

### Get the first item in a list

first_bike = bikes[0]

### Get the last items in a list

first_bike = bikes[-1]


### Looping through a list

for b in bikes:
    print(b)

### Adding items to a list

bikes = []
bikes.append('trek')
bikes.append('redline')
bikes.append('giant')

print(bikes)


### Making numerical lists (การคูณ x^2 เข้าไปในทุกตัวใน list)

squares = []
for x in range(1,11):
    squares.append(x**2)

print(squares)

### List comprehension (List Understanding) (คือการคูณ x^2 เข้าไปทุกตัวใน list อีกแบบนึง ซึ่งถ้าใช้ .append มันจะเป็นการเพิมเข้าไป จะใช้ได้ครั้งเดียว)

squares = [x**2 for x in range(1,11)]

print(squares)


### Sort an alphabet(string/char) in list ///numerical can not sort

name = ['liony', 'slice', 'bunny', 'alice', 'corp']
name.sort()
print(name)



### Slicing a list (หั่น List เป็นท่อนๆ)

finishers = ['sam', 'bob', 'john', 'box']
first_two = finishers[:2]
last_two = [finishers[-1] +', '+ finishers[-2]]

print(first_two)
print(last_two)


### Copying a list

bikes = ['sumo', 'takken', 'golf']

copy_of_bikes = bikes[:]

print(copy_of_bikes)











