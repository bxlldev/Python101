import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as myfile:
        fw = csv.writer(myfile) #fw = file writer
        fw.writerow(datalist) # datalist = ['pen','pencil','eraser']


def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as myfile:
        fr = csv.reader(myfile) #fw = file reader
        data = list(fr)
    return data

data = readcsv()
print(data)


#data = ['ขนมเยลลี่', 20, '7.00o น.']
#writecsv(data)