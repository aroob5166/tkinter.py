from tkinter import *

window = Tk()

entry = Entry(window, width = 35, borderwidth = 5)
entry.grid(row = 0, column = 0, columnspan = 3 , padx = 10, pady = 10)
def click(number):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0, str(current) + str(number))
    
def add():
    firstNum = entry.get()
    entry.delete(0,END)
    entry.insert(0, str(firstNum) + '+')
def subtract():
    
    firstNum = entry.get()
    entry.delete(0,END)
    entry.insert(0, str(firstNum) + '-')
def multiply():
    firstNum = entry.get()
    entry.delete(0,END)
    entry.insert(0, str(firstNum) + '*')
def divide():
    firstNum = entry.get()
    entry.delete(0,END)
    entry.insert(0, str(firstNum) + '/')
def equal():
    exp = entry.get()
    res = eval(exp)
    entry.delete(0,END)
    entry.insert(0,res)
def clear():
    entry.delete(0,END)

button1 = Button(window, text = "1", padx=40, pady = 20, command = lambda: click(1))
button2 = Button(window, text = "2", padx=40, pady = 20, command = lambda: click(2))
button3 = Button(window, text = "3", padx=40, pady = 20, command = lambda: click(3))
button4 = Button(window, text = "4", padx=40, pady = 20, command = lambda: click(4))
button5 = Button(window, text = "5", padx=40, pady = 20, command = lambda: click(5))
button6 = Button(window, text = "6", padx=40, pady = 20, command = lambda: click(6))
button7 = Button(window, text = "7", padx=40, pady = 20, command = lambda: click(7))
button8 = Button(window, text = "8", padx=40, pady = 20, command = lambda: click(8))
button9 = Button(window, text = "9", padx=40, pady = 20, command = lambda: click(9))
button0 = Button(window, text = "0", padx=40, pady = 20, command = lambda: click(0))
buttonadd = Button(window, text = "+", padx=40, pady = 20 , command = add)
buttonsubtract = Button(window, text = "-", padx=40, pady = 20, command = subtract)
buttonmultiply = Button(window, text = "*", padx=40, pady = 20, command = multiply)
buttondivide = Button(window, text = "/", padx=40, pady = 20, command = divide)
buttonequal = Button(window, text = "=", padx=80, pady = 20, command = equal)
buttonclear = Button(window, text = "C", padx=80, pady = 20, command = clear)

button1.grid(row = 3,column =0)
button2.grid(row = 3,column =1)
button3.grid(row = 3,column =2)
button4.grid(row = 2,column =0)
button5.grid(row = 2,column =1)
button6.grid(row = 2,column =2)
button7.grid(row = 1,column =0)
button8.grid(row = 1,column =1)
button9.grid(row = 1,column =2)
button0.grid(row = 4,column =2)
buttonadd.grid(row = 5,column =0)
buttonsubtract.grid(row = 6,column =0)
buttonmultiply.grid(row = 6,column =1)
buttondivide.grid(row = 6,column =2)
buttonequal.grid(row = 5,column =1, columnspan = 2)
buttonclear.grid(row = 4,column =0, columnspan = 2)

mainloop()

