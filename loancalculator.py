from tkinter import  *

def calculate():
    a1=float(e1.get())
    b2=float(e2.get())
    c2=float(e3.get())
    c3=(c2/(100*12))
    resul=(a1 *(c3*((1+c3)**b2)))/(((1+c3)**b2)-1)
    label1.set(resul)


window=Tk()
label1=StringVar();
window.title("Loan Calculator")
Label(window,text="Name").grid(row=0,sticky=W)
Label(window,text="Address").grid(row=1,sticky=W)
Label(window,text="Contact number").grid(row=2,sticky=W)
Label(window,text="Enter loan amount").grid(row=3,sticky=W)
Label(window,text="Enter amount of months to pay").grid(row=4,sticky=W)
Label(window,text="Interest rate").grid(row=5,sticky=W)
Label(window,text="Monthly Amortization").grid(row=6,sticky=W)
result=Label(window,text="", textvariable=label1).grid(row=6, column=1,sticky=W)
e1=Entry(window)
e2=Entry(window)
e3=Entry(window)
e4=Entry(window)
e5=Entry(window)
e6=Entry(window)

e1.grid(row=3,column=1)
e2.grid(row=4,column=1)
e3.grid(row=5,column=1)
e4.grid(row=0,column=1)
e5.grid(row=1,column=1)
e6.grid(row=2,column=1)
b=Button(window,text="Calculate",command=calculate)
b.grid(row=0,column=2)

mainloop()