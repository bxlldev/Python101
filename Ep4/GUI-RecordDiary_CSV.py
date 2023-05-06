from tkinter import * 
from tkinter import ttk # import theme of tk
from tkinter import messagebox # import messagebox เพื่อจะใส่คำสั่งให้กับปุ่มกด
import tkinter as tk
import csv


######################CSV#########################
def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as myfile:
        fw = csv.writer(myfile) #fw = file writer
        fw.writerow(datalist) # datalist = ['pen','pencil','eraser']


def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as myfile:
        fr = csv.reader(myfile) #fr = file reader
        data = list(fr)
    return data

######################CSV#########################


GUI = Tk() # หน้าจอหลักของโปรแกรม
GUI.title('Record My Diary') # ชื่อของโปรแกรม
GUI.geometry("1200x600") # ขนาดของโปรแกรม
#canvas = tk.Canvas(GUI, bg="#808080")

##########Background#############################
canvas = tk.Canvas(GUI, width=1200, height=1200)
image_file = tk.PhotoImage(file="bg3.png")
canvas.create_image(0, 0, image=image_file, anchor="nw")
canvas.pack(fill=tk.BOTH, expand=True)
##########Background#############################


#Header
L1 = Label(GUI,text='My Diary Recording',font=('Tahoma',30,'bold'),fg='black')
L1.place(x=450,y=50)




#########SECTION RIGHT#############
LF1 = ttk.LabelFrame(GUI, text='Hi What about your day :)')
LF1.place(x=500,y=200)

#LF2 = ttk.LabelFrame(GUI, text='Read your diary note')
#LF2.place(x=660,y=320)

v_data = StringVar() #ตัวแปรพิเศษที่ใช้กับข้อความใน GUI
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Tahoma',15,'bold'))
E1.pack(pady=10,padx=10)

from datetime import datetime


def SaveData():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data.get() #ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    text = [t,data] # [เวลา , ข้อมูลที่ได้จากการกรอก]
    writecsv(text) #บันทึกลง CSV
    v_data.set('') #เคลียร์ข้อมูลในช่องกรอก

B1 = ttk.Button(LF1,text='Enter',command=SaveData)
B1.pack(ipadx=10,ipady=10)


def Readme():
    readcsv()
    text = readcsv()
    messagebox.showinfo('Your Diary', text) #showinfo
    


B2 = ttk.Button(LF1,text='Read Your Diary',command=Readme)
B2.pack(ipadx=10,ipady=10)







GUI.mainloop()
