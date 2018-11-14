from tkinter import *
root=Tk()
class clicktyp:
    def __init__(self, master):
        frame=Frame(master)
        frame.pack()
        self.print=Button(root,text="ankush banik",command=self.printmassage)
        self.print.pack()
        self.quit=Button(root,text="quit",command=frame.quit)
        self.quit.pack()
    def printmassage(self):
        print("ankush banik.com")


c=clicktyp(root)


root.mainloop()