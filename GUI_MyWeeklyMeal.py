from tkinter import *
from PIL import Image, ImageTk #image

from tkinter import ttk #theme
from tkinter import messagebox

####################################

# Create a GUI interface
GUI = Tk()
GUI.title('My Diary')
GUI.geometry('1400x1400') # GUI Volume

# Open and resize the image
image1 = Image.open("Pizza.jpg")
image1 = image1.resize((50, 50), Image.LANCZOS)

image2 = Image.open("Spaghetti.jpg")
image2 = image2.resize((50, 50), Image.LANCZOS)

image3 = Image.open("Somtum.jpg")
image3 = image3.resize((50, 50), Image.LANCZOS)

image4 = Image.open("Spaghetti.jpg")
image4 = image4.resize((50, 50), Image.LANCZOS)

image5 = Image.open("7ElevenRice.jpg")
image5 = image5.resize((50, 50), Image.LANCZOS)

image6 = Image.open("GrabFood.png")
image6 = image6.resize((50, 50), Image.LANCZOS)

image7 = Image.open("Hotpot.jpg")
image7 = image7.resize((50, 50), Image.LANCZOS)

# Convert the image to a PhotoImage objet
photo1 = ImageTk.PhotoImage(image1)
photo2 = ImageTk.PhotoImage(image2)
photo3 = ImageTk.PhotoImage(image3)
photo4 = ImageTk.PhotoImage(image4)
photo5 = ImageTk.PhotoImage(image5)
photo6 = ImageTk.PhotoImage(image6)
photo7 = ImageTk.PhotoImage(image7)

# Creata a lable with font
L0 = Label(GUI, text='My weekly meal', font=('Angsana New', 30), fg='#616161')
L0.pack()

# Create a label with the image
L1 = Label(GUI, image=photo1)
#L1.pack(ipadx=50, ipady=40)
L1.place(x=700, y=100)

L2 = Label(GUI, image=photo2)
L2.place(x=700, y=200)

L3 = Label(GUI, image=photo3)
L3.place(x=700, y=300)

L4 = Label(GUI, image=photo4)
L4.place(x=700, y=400)

L5 = Label(GUI, image=photo5)
L5.place(x=700, y=500)

L6 = Label(GUI, image=photo6)
L6.place(x=700, y=600)

L7 = Label(GUI, image=photo7)
L7.place(x=700, y=700)


####################################

def Button1():
    text = 'Pizza'
    messagebox.showinfo('Main cause', text)

FB1 = Frame(GUI)
FB1.place(x=500,y=100)
B1 = ttk.Button(FB1, text='Sunday', command=Button1)
B1.pack(ipadx=20, ipady=20)

####################################
def Button2():
    text = 'Spaghetti'
    messagebox.showinfo('Main cause', text)

FB2 = Frame(GUI)
FB2.place(x=500,y=200)
B2 = ttk.Button(FB2, text='Monday', command=Button2)
B2.pack(ipadx=20, ipady=20)

####################################
def Button3():
    text = 'Papaya Salad'
    messagebox.showinfo('Main cause', text)

FB3 = Frame(GUI)
FB3.place(x=500,y=300)
B3 = ttk.Button(FB3, text='Tuesday', command=Button3)
B3.pack(ipadx=20, ipady=20)

####################################
def Button4():
    text = 'Street Food'
    messagebox.showinfo('Main cause', text)

FB4 = Frame(GUI)
FB4.place(x=500,y=400)
B4 = ttk.Button(FB4, text='Wednesday', command=Button4)
B4.pack(ipadx=20, ipady=20)

####################################
def Button5():
    text = '7-Eleven rice'
    messagebox.showinfo('Main cause', text)

FB5 = Frame(GUI)
FB5.place(x=500,y=500)
B5 = ttk.Button(FB5, text='Thursday', command=Button5)
B5.pack(ipadx=20, ipady=20)

####################################
def Button6():
    text = 'Grab Food'
    messagebox.showinfo('Main cause', text)

FB6 = Frame(GUI)
FB6.place(x=500,y=600)
B6 = ttk.Button(FB6, text='Friday', command=Button6)
B6.pack(ipadx=20, ipady=20)

####################################
def Button7():
    text = 'Hotpot'
    messagebox.showinfo('Main cause', text)

FB7 = Frame(GUI)
FB7.place(x=500,y=700)
B7 = ttk.Button(FB7, text='Saturday', command=Button7)
B7.pack(ipadx=20, ipady=20)


# Run GUI interface
GUI.mainloop()
