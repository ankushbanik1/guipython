from tkinter import *
root=Tk()
root.geometry("200x300")
def fun1():
    print("ankush")
menu=Menu(root)
root.config(menu=menu)
submenu=Menu(menu)
menu.add_cascade(label="file",menu=submenu)
submenu.add_command(label="new open",command=fun1)












root.mainloop()
