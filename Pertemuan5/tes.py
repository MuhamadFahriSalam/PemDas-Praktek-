from tkinter import *

root = Tk()
root.geometry("1000x500")
root.title("Bill Bayar")
root.resizable(False,False)

def Reset():
    entry_PisangGoreng.delete(0,END)
    entry_TempeGoreng.delete(0,END)
    entry_TahuGoreng.delete(0,END)
    entry_BakwanGoreng.delete(0,END)
    entry_EsCincau.delete(0,END)
    entry_EsBlewah.delete(0,END)

def Total():
    try:a1=int(PisangGoreng.get())
    except:a1=0

    try:a2=int(TempeGoreng.get())
    except:a2=0

    try:a3=int(TahuGoreng.get())
    except:a3=0

    try:a4=int(BakwanGoreng.get())
    except:a4=0

    try:a5=int(UbiGoreng.get())
    except:a5=0

    try:a6=int(EsCincau.get())
    except:a6=0

    try:a7=int(EsBlewah.get())
    except:a7=0

    #define cost of each item per quantity
    c1 = 2000 * a1
    c2 = 1500 * a2
    c3 = 1000 * a3
    c4 = 2000 * a4
    c5 = 2000 * a5
    c6 = 3000 * a6
    c7 = 3000 * a7

    lbl_total=Label(f2,font=('aria',20,'bold'),text="Total",width=16,fg="lightyellow",bg="black")
    lbl_total.place(x=0,y=50)

    entry_total=Entry(f2,font=('aria',20,'bold'),textvariable=Total_bill,bd=6,width=15,bg="lightgreen")
    entry_total.place(x=20,y=100)

    totalcost=c1+c2+c3+c4+c5+c6+c7
    string_bill="Rp.",str('%.2f' %totalcost)
    Total_bill.set(string_bill)


Label(text="Bill MANAGEMENT",bg="black",fg="white",font=("calibri",33),width="300",height="2").pack()

#Menu Card
f = Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)
Label(f,font=("Lucida Calilligraphy",15,'bold'),text="PisangGoreng...Rp.2000/pack",fg="black",bg="lightgreen").place(x=10,y=80)
Label(f,font=("Lucida Calilligraphy",15,'bold'),text="TempeGoreng....Rp.1500/pack",fg="black",bg="lightgreen").place(x=10,y=110)
Label(f,font=("Lucida Calilligraphy",15,'bold'),text="TahuGoreng.....Rp.1000/pack",fg="black",bg="lightgreen").place(x=10,y=140)
Label(f,font=("Lucida Calilligraphy",15,'bold'),text="BakwanGoreng...Rp.2000/pack",fg="black",bg="lightgreen").place(x=10,y=170)
Label(f,font=("Lucida Calilligraphy",15,'bold'),text="UbiGoreng......Rp.2000/pack",fg="black",bg="lightgreen").place(x=10,y=200)
Label(f,font=("Lucida Calilligraphy",15,'bold'),text="EsCincau.......Rp.3000/Pack",fg="black",bg="lightgreen").place(x=10,y=230)
Label(f,font=("Lucida Calilligraphy",15,'bold'),text="EsBlewah.......Rp.3000/pack",fg="black",bg="lightgreen").place(x=10,y=260)

#BIll
f2=Frame(root,bg="lightyellow",highlightbackground="bLack",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text="Bill",font=('calibri',20),bg="lightyellow")
Bill.place(x=120,y=10)

#Entry Work
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

PisangGoreng=StringVar()
TempeGoreng=StringVar()
TahuGoreng=StringVar()
BakwanGoreng=StringVar()
UbiGoreng=StringVar()
EsCincau=StringVar()
EsBlewah=StringVar()
Total_bill = StringVar()


#Label
lbl_PisangGoreng=Label(f1,font=("aria",20,'bold'),text="PisangGoreng",width="12",fg="blue4")
lbl_PisangGoreng.grid(row=1,column=0)
lbl_TempeGoreng=Label(f1,font=("aria",20,'bold'),text="TempeGoreng",width="12",fg="blue4")
lbl_TempeGoreng.grid(row=2,column=0)
lbl_TahuGoreng=Label(f1,font=("aria",20,'bold'),text="TahuGoreng",width="12",fg="blue4")
lbl_TahuGoreng.grid(row=3,column=0)
lbl_BakwanGoreng=Label(f1,font=("aria",20,'bold'),text="BakwanGoreng",width="12",fg="blue4")
lbl_BakwanGoreng.grid(row=4,column=0)
lbl_UbiGoreng=Label(f1,font=("aria",20,'bold'),text="UbiGoreng",width="12",fg="blue4")
lbl_UbiGoreng.grid(row=5,column=0)
lbl_EsCincau=Label(f1,font=("aria",20,'bold'),text="EsCincau",width="12",fg="blue4")
lbl_EsCincau.grid(row=6,column=0)
lbl_EsBlewah=Label(f1,font=("aria",20,'bold'),text="EsBlewah",width="12",fg="blue4")
lbl_EsBlewah.grid(row=7,column=0)

#Entry
entry_PisangGoreng=Entry(f1,font=("aria",20,'bold'),textvariable=PisangGoreng,bd=6,width=8,bg="lightpink")
entry_PisangGoreng.grid(row=1,column=1)
entry_TempeGoreng=Entry(f1,font=("aria",20,'bold'),textvariable=TempeGoreng,bd=6,width=8,bg="lightpink")
entry_TempeGoreng.grid(row=2,column=1)
entry_TahuGoreng=Entry(f1,font=("aria",20,'bold'),textvariable=TahuGoreng,bd=6,width=8,bg="lightpink")
entry_TahuGoreng.grid(row=3,column=1)
entry_BakwanGoreng=Entry(f1,font=("aria",20,'bold'),textvariable=BakwanGoreng,bd=6,width=8,bg="lightpink")
entry_BakwanGoreng.grid(row=4,column=1)
entry_UbiGoreng=Entry(f1,font=("aria",20,'bold'),textvariable=UbiGoreng,bd=6,width=8,bg="lightpink")
entry_UbiGoreng.grid(row=5,column=1)
entry_EsCincau=Entry(f1,font=("aria",20,'bold'),textvariable=EsCincau,bd=6,width=8,bg="lightpink")
entry_EsCincau.grid(row=6,column=1)
entry_EsBlewah=Entry(f1,font=("aria",20,'bold'),textvariable=EsBlewah,bd=6,width=8,bg="lightpink")
entry_EsBlewah.grid(row=7,column=1)

#Buttons
btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)

root.mainloop()