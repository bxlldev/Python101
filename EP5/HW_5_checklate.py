Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def checklate(employee):
...     for em in employee.items():
...         if em[1] >= 9.00:
...             print(em[0],em[1])
... 
...             
>>> 

>>> employee = {
... 'somchai':8.45,
... 'somsak':8.55,
... 'somsuk':9.05,
... 'sommai':10.00,
... 'somboon':8.30,
... 'sompong':9.04,
... 'somsri':8.25
... }
>>> 
>>> 
>>> 
>>> checklate(employee)
somsuk 9.05
sommai 10.0
sompong 9.04
>>> 
