Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

===== RESTART: C:\Users\Thanachart Saejueng\Desktop\Python\Ep4\writefile.py ====

===== RESTART: C:\Users\Thanachart Saejueng\Desktop\Python\Ep4\writefile.py ====

===== RESTART: C:\Users\Thanachart Saejueng\Desktop\Python\Ep4\writefile.py ====

===== RESTART: C:\Users\Thanachart Saejueng\Desktop\Python\Ep4\writefile.py ====
['ซื้อน้ำเต้าหู้หน้าปากซอย 10 บาทซื้อลูกอม 5 บาท\n', 'ซื้อไม้บรรทัด 5 บาท\n', 'ซื้อสมุด 15 บาท\n', 'ซื้อยางลบ 5 บาท\n']

===== RESTART: C:\Users\Thanachart Saejueng\Desktop\Python\Ep4\writefile.py ====

===== RESTART: C:\Users\Thanachart Saejueng\Desktop\Python\Ep4\writefile.py ====
<function readdata at 0x0000018DBB179440>

====== RESTART: C:\Users\Thanachart Saejueng\Desktop\Python\Ep4\writefile.py ======

====== RESTART: C:\Users\Thanachart Saejueng\Desktop\Python\Ep4\writefile.py ======
Traceback (most recent call last):
  File "C:\Users\Thanachart Saejueng\Desktop\Python\Ep4\writefile.py", line 22, in <module>
    readdata()
NameError: name 'readdata' is not defined. Did you mean: 'readdata2'?

====== RESTART: C:\Users\Thanachart Saejueng\Desktop\Python\Ep4\writefile.py ======

====== RESTART: C:\Users\Thanachart Saejueng\Desktop\Python\Ep4\writefile.py ======

====== RESTART: C:\Users\Thanachart Saejueng\Desktop\Python\Ep4\writefile.py ======
ซื้อน้ำเต้าหู้หน้าปากซอย 10 บาทซื้อลูกอม 5 บาท
ซื้อไม้บรรทัด 5 บาท
ซื้อสมุด 15 บาท
ซื้อยางลบ 5 บาท


====== RESTART: C:\Users\Thanachart Saejueng\Desktop\Python\Ep4\writefile.py ======
['ซื้อน้ำเต้าหู้หน้าปากซอย 10 บาทซื้อลูกอม 5 บาท\n', 'ซื้อไม้บรรทัด 5 บาท\n', 'ซื้อสมุด 15 บาท\n', 'ซื้อยางลบ 5 บาท\n']

====== RESTART: C:\Users\Thanachart Saejueng\Desktop\Python\Ep4\writefile.py ======
['ซื้อน้ำเต้าหู้หน้าปากซอย 10 บาทซื้อลูกอม 5 บาท\n', 'ซื้อไม้บรรทัด 5 บาท\n', 'ซื้อสมุด 15 บาท\n', 'ซื้อยางลบ 5 บาท\n']

====== RESTART: C:\Users\Thanachart Saejueng\Desktop\Python\Ep4\writefile.py ======
['ซื้อน้ำเต้าหู้หน้าปากซอย 10 บาทซื้อลูกอม 5 บาท\n', 'ซื้อไม้บรรทัด 5 บาท\n', 'ซื้อสมุด 15 บาท\n', 'ซื้อยางลบ 5 บาท\n']

====== RESTART: C:\Users\Thanachart Saejueng\Desktop\Python\Ep4\writefile.py ======
['ซื้อน้ำเต้าหู้หน้าปากซอย 10 บาทซื้อลูกอม 5 บาท\n', 'ซื้อไม้บรรทัด 5 บาท\n', 'ซื้อสมุด 15 บาท\n', 'ซื้อยางลบ 5 บาท\n']

====== RESTART: C:\Users\Thanachart Saejueng\Desktop\Python\Ep4\writefile.py ======
ซื้อน้ำเต้าหู้หน้าปากซอย 10 บาทซื้อลูกอม 5 บาท
ซื้อไม้บรรทัด 5 บาท
ซื้อสมุด 15 บาท
ซื้อยางลบ 5 บาท




box = []


box.append('ปากกา')
box.append('ดินสอ')
box.append('ยางลบ')


print(box)
['ปากกา', 'ดินสอ', 'ยางลบ']



print{box[0]}
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
SyntaxError: invalid syntax


print(box[0])
ปากกา





print(box[1])
ดินสอ




print(box[2])
ยางลบ








print(box[-1])
ยางลบ




print(box[-2])
ดินสอ




print(box[-3])
ปากกา





print(box[-4])
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(box[-4])
IndexError: list index out of range







brand = {'Pen': ['Lamy','Pental','FiberCastel'],'Pencil': ['Horse','2B','Steidler'], 'Eraser':['2color','2Beraser']}





print(brand['pen'])
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print(brand['pen'])
KeyError: 'pen'
print(brand['Pen'])
['Lamy', 'Pental', 'FiberCastel']







print(brand['Pen'[1]])
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    print(brand['Pen'[1]])
KeyError: 'e'
print(brand['Pen'][1])
Pental




print(brand['Pen'][2])
FiberCastel



print(brand['Pen'][2])
FiberCastel
print(brand['Pen'][2])
FiberCastel






print(brand['Pencil'][2])
Steidler




print(brand['Eraser'][2])
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    print(brand['Eraser'][2])
IndexError: list index out of range



print(brand['Eraser'][2])brand = {'Pen': ['Lamy','Pental','FiberCastel'],'Pencil': ['Horse','2B','Steidler'], 'Eraser':'2color'}
SyntaxError: invalid syntax


brand = {'Pen': ['Lamy','Pental','FiberCastel'],'Pencil': ['Horse','2B','Steidler'], 'Eraser':['2color','2Beraser']}






print(brand['Pencil'][2])
Steidler






print(box)
['ปากกา', 'ดินสอ', 'ยางลบ']




print(len(box))
3







print(brand.key())
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    print(brand.key())
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
print(brand.key())
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    print(brand.key())
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?





print(brand.keys())
dict_keys(['Pen', 'Pencil', 'Eraser'])




print(brand.values())
dict_values([['Lamy', 'Pental', 'FiberCastel'], ['Horse', '2B', 'Steidler'], ['2color', '2Beraser']])






for b in box:
    print(b)

    
ปากกา
ดินสอ
ยางลบ







for br in brand.keys():
    print(br)

    
Pen
Pencil
Eraser







for br in brand.values():
    print(br)

    
['Lamy', 'Pental', 'FiberCastel']
['Horse', '2B', 'Steidler']
['2color', '2Beraser']

>>> 
>>> 
>>> 
>>> 
>>> for br in brand:
...     print(br)
... 
...     
Pen
Pencil
Eraser
>>> 
>>> 
>>> 
>>> for br in brand.items():
...     print(br)
... 
...     
('Pen', ['Lamy', 'Pental', 'FiberCastel'])
('Pencil', ['Horse', '2B', 'Steidler'])
('Eraser', ['2color', '2Beraser'])
>>> 
>>> 
>>> 
>>> 
>>> len(brand)
3
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
