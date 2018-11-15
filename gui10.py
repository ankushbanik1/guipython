from tkinter import *
def dowonload ():
    print("hello")
m=Tk()

######################   toolbar    ##############################

toolbar=Frame(m,bg="blue")
insurtbut = Button(toolbar,text="insurt image", command=dowonload)
insurtbut.pack(side=LEFT,padx=2,pady=2)
insurtbut1 = Button(toolbar,text="image", command=dowonload)
insurtbut1.pack(side=LEFT,padx=2,pady=2)
toolbar.pack(side=TOP)

m.mainloop()
