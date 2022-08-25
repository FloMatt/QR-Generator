# Importing the modules
from tkinter import *
import time
import pyqrcode


def qr_genrt():
    global qr, img
    qr = pyqrcode.QRCode(con.get())
    qr_xbm = qr.xbm(scale=10)
    img = BitmapImage(data=qr_xbm, foreground='black', background='white')
    l3.config(image=img)


def save():
    qr_genrt()
    tme = time.time()
    qr.png(f'{tme}.png', scale=10)
    con.set('')

# Main program


wind = Tk()
wind.title('QR Code Generator')
wind.geometry('800x800')
wind.resizable()

# Variable
con = StringVar()

f1 = Frame(wind, width=500, height=100)
f1.pack()
f2 = Frame(wind, width=500, height=50)
f2.pack()
f3 = Frame(wind, width=500, height=250)
f3.pack()

l1 = Label(f1, text='QR Code Generator', font=('Helvetica', 30, 'bold'))
l1.grid(row=0, column=0, columnspan=3, padx=5, pady=10)
l2 = Label(f2, font=('', 12), text='Enter the number, text or url:')
l2.grid(row=0, column=0, padx=5)

e1 = Entry(f2, textvariable=con, width=40)
e1.grid(row=0, column=1, padx=5)

b1 = Button(f2, text='Generate QR', command=qr_genrt)
b1.grid(row=1, column=0, pady=10)

b2 = Button(f2, text='Save', command=save)
b2.grid(row=1, column=1, pady=10)

l3 = Label(f3, pady=5)
l3.pack()

wind.mainloop()
