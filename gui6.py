from tkinter import *
root=Tk()
def printname(Event):
    print("ankush banik")
button1=Button(root, text="print name")
button1.bind("<Button-1>",printname)
button1.pack()    





root.mainloop()