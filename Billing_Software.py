from tkinter import *
from tkinter import messagebox
import random
root = Tk()
root.geometry("1350x700")
root.title("Billing Software")
bg_color = "crimson"
#.............VARIABLE...................
c_name = StringVar()
c_phone = StringVar()
item = StringVar()
rte = IntVar()
quant = IntVar()
bill_no = StringVar()
x = random.randint(1,1000)
bill_no.set(str(x))

global l
l = []
#..............FUNCTION...................
def welcome():
        textarea.delete(1.0,END)
        textarea.insert(END,"\t\t WELCOME TO SKM STORE\n MM 222 SECTOR-D ALIGANJ, LUCKNOW, UTTAR PRADESH-226024")
        textarea.insert(END,f"\n---------------------------------------------------------")
        textarea.insert(END,f"\n\nBILL NUMBER    :\t{bill_no.get()}")
        textarea.insert(END,f"\n\nCUSTOMER NAME  :\t{c_name.get()}")
        textarea.insert(END,f"\n\nPHONE NUMBER   :\t{c_phone.get()}")
        textarea.insert(END,f"\n\n---------------------------------------------------------")
        textarea.insert(END,f"\nProduct Name\t\t\tQuantity\t\t\tPrice")
        textarea.insert(END,f"\n---------------------------------------------------------\n")
        #textarea.configure(font="arial 15 bold")

def additem():
        n = rte.get()
        m = quant.get() * n
        l.append(m)
        if item.get()=='':
                messagebox.showerror("ERROR!","Please Enter The Item!!")
        else:
                textarea.insert(END,f"\n     {item.get()}\t\t\t   {quant.get()}\t\t\t {m}")

def genbill():
        if c_name.get() == '' and c_phone.get() == '':
                messagebox.showerror("ERROR","CUSTOMER DETAILS ARE MUST!!")
        else:
                t = textarea.get(15.0,(15.0+float(len(l))))
                welcome()
                textarea.insert(END,t)
                textarea.insert(END,f"\n\n---------------------------------------------------------")
                textarea.insert(END,f"\t\t\t\t\t\tNET AMOUNT: \t\t{sum(l)}")
                textarea.insert(END,f"\n---------------------------------------------------------")
                #textarea.insert(END,f"\n---------------------------------------------------------\n")
                textarea.insert(END,"\t\t     THANK YOU, FOR SHOPPING WITH US!!")
                textarea.insert(END,f"\n---------------------------------------------------------\n")
                savebill()

def savebill():
        op = messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
                bill_details = textarea.get(1.0,END)
                f1=open("Bills"+str(bill_no.get())+".txt",'w')
                f1.write(bill_details)
                f1.close()
                messagebox.showinfo("Saved",f"Bill Number {bill_no.get()} saved successfully!")
        else:
                return

def clear():
        c_name.set("")
        c_phone.set("")
        item.set("")
        rte.set(0)
        quant.set(0)
        welcome()

def exit():
        op = messagebox.askyesnocancel("EXIT","Do you really want to exit?")
        if op>0:
                root.destroy()
        else:
                return        
#..........TOP SECTION...............
title = Label(text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
#..........CUSTOMER DETAILS..........
F1 = LabelFrame(text="Customer Details",bg=bg_color,fg="gold",font=("times new roman",15,"bold"))
F1.place(x=0,y=80,relwidth=1)
cname_lbl = Label(F1,text="Customer Name",font=("times new roman",15,"bold"),bg=bg_color,fg="white")
cname_lbl.grid(row=0,column=0,padx=10,pady=5)
cname_txt = Entry(F1,width=15,font="arial 15 bold",relief=SUNKEN,textvariable=c_name)
cname_txt.grid(row=0,column=1,padx=10,pady=5)

cphno_lbl = Label(F1,text="Phone Number",font=("times new roman",15,"bold"),bg=bg_color,fg="white")
cphno_lbl.grid(row=0,column=2,padx=10,pady=5)
cphno_txt = Entry(F1,width=15,font="arial 15 bold",relief=SUNKEN,textvariable=c_phone)
cphno_txt.grid(row=0,column=3,padx=10,pady=5)
#.............PRODUCT DETAILS...........
F2 = LabelFrame(text="Product Details",bg=bg_color,fg="gold",font=("times new roman",15,"bold"))
F2.place(x=100,y=200,width=630,height=500)
itm_lbl = Label(F2,text="Product Name",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen")
itm_lbl.grid(row=0,column=0,padx=30,pady=20)
itm_txt = Entry(F2,width=20,font="arial 15 bold",textvariable=item)
itm_txt.grid(row=0,column=1,padx=30,pady=20)

quantity_lbl = Label(F2,text="Product Quantity",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen")
quantity_lbl.grid(row=1,column=0,padx=30,pady=20)
quantity_txt = Entry(F2,width=20,font="arial 15 bold",textvariable=quant)
quantity_txt.grid(row=1,column=1,padx=30,pady=20)

rate_lbl = Label(F2,text="Product Rate",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen")
rate_lbl.grid(row=2,column=0,padx=30,pady=20)
rate_txt = Entry(F2,width=20,font="arial 15 bold",textvariable=rte)
rate_txt.grid(row=2,column=1,padx=30,pady=20) 
#...........BUTTONS..................
btn1 = Button(F2,text="ADD ITEM",font="arial 15 bold",pady=10,bg='Blue',width=20,command=additem)
btn1.grid(row=3,column=0,padx=20,pady=30)   

btn2 = Button(F2,text="GENERATE BILL",font="arial 15 bold",pady=10,bg='Blue',width=20,command=genbill)
btn2.grid(row=3,column=1,padx=20,pady=30) 

btn3 = Button(F2,text="CLEAR",font="arial 15 bold",pady=10,bg='Black',fg="white",width=20,command=clear)
btn3.grid(row=4,column=0,padx=20,pady=30) 

btn4 = Button(F2,text="EXIT",font="arial 15 bold",pady=10,bg='Black',fg="white",width=20,command=exit)
btn4.grid(row=4,column=1,padx=20,pady=30)
#..............BILL AREA..............
F3 = Frame(root,relief=GROOVE,bd=10)
F3.place(x=800,y=200,width=500,height=500)    
bill_title = Label(F3,text="BILL AREA",font=('arial 15 bold'),relief=GROOVE,bd=7).pack(fill=X) 
scroll = Scrollbar(F3,orient=VERTICAL)
textarea=Text(F3,yscrollcommand=scroll)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=textarea.yview)
textarea.pack()
welcome()
root.mainloop()