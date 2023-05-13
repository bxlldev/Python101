Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> prompt = "How many ticket do you need? :"
>>> 
>>> num_ticket = input(prompt)
How many ticket do you need? :5
>>> 
>>> 
>>> 
>>> try:
...     num_ticket = int(num_ticket)
... except ValueError:
...     print("Please try again..")
... else:
...     print("Your ticket are printing soon!")
... 
...     
Your ticket are printing soon!
