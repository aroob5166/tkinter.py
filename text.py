from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename , asksaveasfilename
import os


def newFile():
    global file
    window.title("Untiled - Notepad")
    file = None
    textArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension = ".txt", filetypes = [
                           ("All Files",'*.*'),("Text Documents","*.txt*")])

    print(file)

    if file == "":
        file = None
    else:
        window.title(os.path.basename(file)+ " -Notepad")
        textArea.delete(1.0, END)
        content = open(file , "r")
        textArea.insert(1.0, content.read())
        content.close()
def saveFile():
    data = [('All types(*.*)', '*.*')]
    file = asksaveasfilename(filetypes = data, defaultextension = data)  
   
        
    if file == "":
           file = None
    else:
        window.title(os.path.basename(file)+ " -Notepad")
        
        content = open(file , "w")
        content.write(textArea.get(1.0, END))
        content.close()   
      

def exitApp():
    window.destroy()
def cut():
    textArea.event_generate(("<<Cut>>"))
def copy():
    textArea.event_generate(("<<Copy>>"))
def paste():
     textArea.event_generate(("<<Paste>>"))
def about():
    showinfo('Notepad','This is notepad created by Aroob')

if __name__ == "__main__":
    window = Tk()
    window.title('Untitled - Notepad')
    window.iconbitmap('py.ico')
    window.geometry("1200x600")
    # Text area
    textArea = Text(window, font = "roboto")
    fill = None
    print(fill)
    textArea.pack(expand = True , fill = BOTH)
    # Menu bar
    menuBar = Menu(window)

    # File menu
    fileMenu = Menu(menuBar, tearoff = 0)
    fileMenu.add_command(label="New", command=newFile)
    fileMenu.add_command(label="Open", command=openFile)
    fileMenu.add_command(label="Save", command=saveFile)
    

    fileMenu.add_separator()

    fileMenu.add_command(label="Exit", command=exitApp)
    menuBar.add_cascade(label="File", menu=fileMenu)

    #Edit menu
    editMenu = Menu(menuBar, tearoff = 0)
    editMenu.add_command(label="Cut", command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)
    menuBar.add_cascade(label="Edit", menu=editMenu)
    #Help menu
    helpMenu = Menu(menuBar, tearoff = 0)
    helpMenu.add_command(label="About", command=about)
    menuBar.add_cascade(label="Help", menu=helpMenu)

    window.config(menu = menuBar)
    # Add scroll bar
    scroll = Scrollbar(textArea)
    scroll.pack(side= RIGHT, fill = Y )
    scroll.config(command = textArea.yview)
    textArea.config(yscrollcommand = scroll.set)

    window.mainloop()
    