#writefile.py
# ใส่ encoding='utf-8' เพื่อให้ใส่ภาษาไทยได้

#write แบบ function
def writedata():
    with open('data.txt','w', encoding='utf-8') as myfile:
        myfile.write('สบายดีมั้ย?')
    
    

def adddata(text):
    with open('add-data.txt','a', encoding='utf-8') as myfile:
        myfile.writelines(text + '\n')


def readdata():
    with open('add-data.txt', encoding='utf-8') as myfile:
        #data = myfile.readlines() #export to list
        data = myfile.read()
        print(data)

readdata()




        
#write แบบ function CSV file      
#adddata('ซื้อไม้บรรทัด 5 บาท')
#adddata('ซื้อสมุด 15 บาท')
#adddata('ซื้อยางลบ 5 บาท')




