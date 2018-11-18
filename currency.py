from tkinter import *
root=Tk()
root.geometry("400x400+250+250")

heading= Label(root, text="wellcome", font=("arial",13,"bold"), fg="steelblue").pack()
entr_amt = Label(root, text="enter amount in doller", font=("arial",13,"bold")).place(x=10, y=50)

my_num = IntVar()
ent_box = Entry(root, width= 50 , textvariable=my_num).place(x=10, y= 90)


def converter():
    here =my_num.get()
    final= here* 69.2
    lab1=Label(root, text=("Rs."+ str(final)), font=("arial 25 bold"), fg= "red").place(x=10, y=200)

def reverse():
    here =my_num.get()
    final= here/ 69.2
    lab=Label(root, text=("$."+ str(final)), font=("arial 25 bold"), fg= "green").place(x=100, y=240)

button1= Button(root,text="Concvert", width=12, height=2, bg= "lightgreen", command=converter).place(x=10 , y = 130)    

button1= Button(root,text="Reverse", width=12, height=2, bg= "lightgreen", command=reverse).place(x=180 , y = 130)    


































root.mainloop()