
# Exceptions

## Exceptions help you respond appropriately to errors that are likely to occur. You place code that might cause an error in the try block. Code that should run in response to an error goes in the except block. Code that should run only if the try block was successful goes in the else block


## Catching an exception
prompt = "How many ticket do you need? :"

num_ticket = input(prompt)


try:
    num_ticket = int(num_ticket)
except ValueError:
    print("Please try again..")
else:
    print("Your ticket are printing soon!")
