from tkinter import *
root=Tk()
def rightclick(event):
    print("right")
def middleclick(event):
    print("middle")
def leftclick(event):
    print("left")

frame=Frame(root, width=200, height=300)
frame.bind("<Button-1>",rightclick)    
frame.bind("<Button-2>",middleclick)  
frame.bind("<Button-3>",leftclick)  
frame.pack()







root.mainloop()
