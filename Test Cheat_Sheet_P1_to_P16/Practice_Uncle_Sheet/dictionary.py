
#Dictionary

# เป็นตัวแปรที่มีรูปแบบในการจัดการข้อมูล โดยมีข้อมูลที่ถูกเก็บไว้แบ่งเป็น 2 แบบหลัก key กับ value

# obtect = {'key': 'value', 'key2': 'value2', ...}

## {'key': 'value'} จะมองเป็น 1 item

# obtect = {item1, item2, ...}

gem = {'Diamond':'Blue Diamond', 'Stone':'Pure Stone'}


print(gem)


# การเรียกค่าใน dict()

print(gem['Diamond'])

print(gem['Stone'])


# การเพิ่มค่าใน dict() โดยจะนับต่อจากที่มีอยู่

gem['Ruby'] = ['Pastal', 'Royal']

print(gem)


gem['Diamond'] = ['Pink']

print(gem)






