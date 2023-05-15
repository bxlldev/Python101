

# List

#การสร้าง list แบบช่วง 100 idex แรก
number1 = list(range(100))

print(number1)


#การสร้าง list แบบกำหนดช่วง index1 ถึง index51
number2 = list(range(1,51))

print(number2)



#การเพิ่มค่าใน list โดยเพิ่มไปที่ตำแหน่งสุดท้าย (index-1)
box = ['A', 'B']

box.append('C')

print(box)



#การแทรกค่าใน list โดยจะแทรกไปใน index ที่เรากำหนด
box.insert(0,'D') #insert index0

print(box)


#การลบค่าใน list โดยจะลบใน index ที่เรากำหนด
box.pop(0) #delete index0
box.pop() #delete index-1

print(box)
