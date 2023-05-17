
#Set

# เป็นค่าที่คล้ายกับ dict() แต่มีเพียง key หรือ ค่าเพียงค่าเดียว (แต่ค่าของ set จะไม่มีการลำดับ)



animal = {'cat','dog','snake','tiger','elephant'}

print(animal)


#การเพิ่มค่าใน set

animal.add('fish')

print(animal)

#การเพิ่มค่าใน set หลายๆค่าพร้อมกัน

animal.update(['owl','bird'])

print(animal)


#การลบค่าใน set แต่ .discard()  จะไม่มี error หากค่าถูกลบไปแล้ว

animal.remove('cat') #ลบได้ทีละค่าเท่านั้นสำหรับ .remove()

print(animal)

animal.discard('dog') #ลบได้ทีละค่าเท่านั้นสำหรับ .discard()

print(animal)






