# Function

#การประกาศ function แบบไม่มี parameter

def first_function():
    print("Hello My name is Thanachart !")

first_function()

#การประกาศ function แบบมี parameter 1 ตัว

def second_function(name):
    print("Hello My name is " + name)

second_function("Thanachart")

second_function("Pornkamol")

#การประกาศ function แบบมี parameter มากกว่า 1 ตัว

def third_function(name,age):
    print("Hello My name is " + name)
    print("I am " + str(age) + " years old")

third_function("Thanachart",23)


#การประกาศ function แบบมี parameter มากกว่า 1 ตัว (สลับตำแหน่งเวลาเรียกใช้งานได้)

def fourth_function(name,age):
    print("Hello My name is " + name)
    print("I am " + str(age) + " years old")
   
fourth_function(name="Thanachart", age=23)
fourth_function(age=23, name="Thanachart")


#การประกาศ function แบบมี parameter มากกว่า 1 ตัว (โดยกำหนดค่า Default ได้)

def fifth_function(name,age=23):
    print("Hello My name is " + name)
    print("I am " + str(age) + " years old")

fifth_function("Thanachart")
fifth_function("Thanachart",50)



#การประกาศ function แบบมี parameter มากกว่า 1 ตัว (โดยกำหนดแบบค่าเป็น None) ถ้าไม่มีการเรียกใช้จะไม่ print ค่าออกมา

def sixth_function(name,age=None):
    print("Hello My name is " + name)
    if age:
        print("I am " + str(age) + " years old")

sixth_function("Thanachart")
sixth_function("Thanachart",23


#การประกาศ function แบบไม่มี parameter (แบบมีการคืนค่ากลับ)

def first2_function():
    return "Hello My name is Thanachart !"

hello = first2_function()

print(hello)


#การประกาศ function แบบมี parameter 1 ตัว (แบบมีการคืนค่ากลับ)

def second2_function(name):
    return "Hello My name is " + name

hello = second2_function("Thanachart")

print(hello)









