from tkinter import *
def dowonload():
    print("hello")
m=Tk()
menu = Menu(m)
m.config(menu=Menu)

m.title("ankush")

submenu=Menu(menu)
menu.add_cascade(label="file",menu=submenu)
submenu.add_command(label="new project",command=dowonload)
submenu.add_separator()
submenu.add_command(label="exit",command=dowonload)
edit=Menu(menu)
menu.add_cascade(label="file",menu=edit)
edit.add_command(label="file",command=dowonload)





m.mainloop()
