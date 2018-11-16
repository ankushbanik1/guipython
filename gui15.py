from tkinter import *
win=Tk()
win.geometry("200x300")
def fun1():
    print("ankush")
menu=Menu(win)
win.config(menu=menu)
subMenu= Menu(menu)
menu.add_cascade(label="file", menu=subMenu)
subMenu.add_command(label="new project", command=fun1)
subMenu.add_command(label="new file",command=fun1)

editMenu=Menu(menu)
menu.add_cascade(label="editing",menu=subMenu)
editMenu.add_command(label="cut",command=fun1)















win.mainloop()