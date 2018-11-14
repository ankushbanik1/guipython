from tkinter import *
root=Tk()
lebel1=Label(root,text="name")
lebel2=Label(root,text="password")
entry1=Entry(root)
entry2=Entry(root)
lebel1.grid(row=0, sticky=E)
lebel2.grid(row=1,sticky=E)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
c=Checkbutton(root, text= "keep me Logged in")
c.grid(column=2)








root.mainloop()