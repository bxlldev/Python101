Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def checkage20(friend):
...     for f in friend.items():
...         if f[1] >= 20:
...             print(f[0], f[1])
... 
...             
>>> 
>>> friend = {
... 'somchai':'17'
... 'somsak':'21'
... 'somsuk':'18'
... 'sommai':'25'
... 'somboon':'29'
... 'sompong':'19'
... 'somsri':'20'
... }
SyntaxError: invalid syntax
>>> 
>>> 
>>> friend = {
... 'somchai':17
... 'somsak':27
... 'somsuk':18
... 'sommai':25
... 'somboon':29
... 'sompong':19
... 'somsri':20
... }
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> 
>>> 
>>> friend = {
... 'somchai':17,
... 'somsak':27,
... 'somsuk':18,
... 'sommai':25,
... 'somboon':29,
'sompong':19,
'somsri':20
}


checkage20(friend)
somsak 27
sommai 25
somboon 29
somsri 20


