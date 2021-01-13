from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
window = Tk()

window.title('My tk window')
window.iconbitmap('py.ico')

window.geometry("400x400")
vertical = Scale(window, from_ = 0, to= 200)
vertical.pack()

horizontal = Scale(window, from_= 200, to = 400 , orient = HORIZONTAL)
horizontal.pack()

def slide():
    x = horizontal.get()
    window.geometry(str(x)+"x400")

Button(window , text="Button",command= slide ).pack()


mainloop()