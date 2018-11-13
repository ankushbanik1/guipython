from tkinter import *
root=Tk()
one=Label(root,text="one",bg="red",fg="green")
one.pack()
sec=Label(root,text="blue",bg="blue",fg="grey")
sec.pack(fill=Y)
thr=Label(root,text="sec",bg="green",fg="red")
thr.pack(side=LEFT,fill=X)







root.mainloop()