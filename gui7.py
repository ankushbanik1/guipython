from tkinter import *
root=Tk()

def rightclick(Event):
     print("right")

def middleclick(Event):
    print("middle")
def leftclick(Event):
    print("left")

fream=Frame(root, width=500, height=300)
fream.bind("<Button-1>", rightclick)        
fream.bind("<Button-1>", middleclick)      
fream.bind("<Button-1>", leftclick)      
fream.pack()     
root.mainloop()