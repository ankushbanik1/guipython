from tkinter import *
from tkinter import filedialog


win=Tk()


win.geometry("200x300")

def fun1():
    print("ankush")
def resize():
    win.geometry("200x200")

def browse():
    filename=filedialog.askopenfilenames(filetype=(("File","*.py"),("All Files","*.*")))
    pathlabale.config(text=filename)


menu=Menu(win)
win.config(menu=menu)
subMenu= Menu(menu)
menu.add_cascade(label="file", menu=subMenu)
subMenu.add_command(label="new project", command=fun1)
subMenu.add_command(label="new file",command=fun1)
subMenu.add_command(label="exit", command=quit)
subMenu.add_command(label="resize",command=resize)
subMenu.add_command(label="open",command=browse)
editMenu=Menu(menu)
menu.add_cascade(label="editing",menu=subMenu)
editMenu.add_command(label="cut",command=fun1)











pathlabel=Label(win)
pathlabel.pack()



win.mainloop()