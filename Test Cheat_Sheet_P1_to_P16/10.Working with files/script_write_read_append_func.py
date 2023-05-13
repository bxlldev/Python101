
# Working with files

## Your programs can "read" from files and "write" to files. Files are opened in read mode ('r') by default, but also be opened in write mode ('w') and append mode ('a').

## Note: Using encoding='utf-8' for accept Thai language



## Writing to files

def writedata():
    with open('testfile.txt', 'w', encoding='utf-8') as myfile:
        myfile.write("สวัสดีชาว DevOps")

#writedata()

## Appending to a file

def adddata():
    with open('testfile.txt', 'a', encoding='utf-8') as myfile:
        myfile.write("\nสวัสดีชาว DevOps v2")
    
#adddata()
        
## Reading a file and storing its lines

def readdata():
    with open('testfile.txt', encoding='utf-8') as myfile:
        #data = myfile.readlines() #export to list
        data = myfile.read()
        print(data)

#readdata()












