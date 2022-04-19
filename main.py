from tkinter import *
import random


win = Tk()
win.geometry("600x300")

lblnb1 = Label(win, text = "Length to generate : ")
lblnb1.place(x = 0, y = 50)
entnb1 = Entry(win)
entnb1.place(x= 200, y= 50)


lblnb2 = Label(win, text = " the generated password : ")
lblnb2.place(x= 0, y= 100)
entnb2 = Entry(win)
entnb2.place(x= 215, y= 100)

def action():
    chars = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890&()§!+=*$€¥£')
    for l in range(int(entnb1.get())):
        Out = random.choice(chars)
        entnb2.delete(l, END)
        entnb2.insert(0, Out)



Valid = Button(win, text= "Valid the entry", command = action)
Valid.place(x=10, y= 150 )



win.mainloop()