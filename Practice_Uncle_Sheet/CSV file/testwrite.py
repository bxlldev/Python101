
#Read and Write File (Text)

## encoding='utf-8' >> Support Thai language

## Writing to files

import csv

def writedata():
    with open('testfile.csv','w',encoding='utf-8',newline='') as myfile:
        data = csv.writer(myfile)
        data.writerow(["Thanachart","Saejueng",23])
        data.writerow(["Pornkamol","Pimpasri",22])
        

#writedata()

## Appending to a file

def adddata():
    with open('testfile.csv', 'a', encoding='utf-8',newline='') as myfile:
        data = csv.writer(myfile)
        data.writerow(["Noname","Nosername",100])
    
#adddata()
        
## Reading a file and storing its lines

def readdata():
    with open('testfile.csv', encoding='utf-8') as myfile:
        read_data = csv.reader(myfile,delimiter=",")
        for row in read_data:
            print(row)
    

#readdata()
