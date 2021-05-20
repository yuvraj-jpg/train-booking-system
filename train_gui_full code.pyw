from tkinter import *
import time
from tkinter.font import Font

box=Tk()
box.title('Train System')
box.geometry("1220x720")
box.maxsize(1220,720)
box.minsize(1220,720)
box.config(bg="red")
lg=LabelFrame(box,text="",bg="lightgreen")
l1=Listbox(box,width=64,height=22,font="times 15",bg="lightgreen")
l1.place(x=567,y=199)

# Train system code
class system:
    def __init__(self,name,price,seat):
        self.name=name
        self.price=price
        self.seat=seat
        self.b=seat      
        Message(box,text=f"Name of the train is { self.name}",font="times 15",width=400,bg="lightgreen").place(x=567,y=90,width=350)  
        Message(box,text=f"Price of the one seat is { self.price}",font="times 15",width=400,bg="lightgreen").place(x=567,y=120,width=220)  
        Message(box,text=f"Total seats in the train Available is { self.seat}",font="times 15",width=400,bg="lightgreen").place(x=567,y=150,width=330)   
        # l1.insert(1,"**************************************************************************")
        l1.insert(1,"                                              CURRENT STATUS")
    def status(self):        
        Message(box,text=f"Total seats in the train Available is { self.seat}",font="times 15",width=400,bg="lightgreen").place(x=567,y=150,width=330)   
    def book(self):
        if(self.seat>0):
            l1.insert(1,f"Your seat no. {self.seat} is BOOKED  ")
            self.seat=self.seat-1
        else:
            l1.insert(1,"SORRY !!! seats are fulll  ")

    def cancel(self):        
        if self.b==self.seat:
            l1.insert(1,"you haved not book any seat ")

        else:
            self.seat=self.seat+1
            l1.insert(1,f"Your seat No. {self.seat} is CANCEL")
p=system("Janta Express : 14407",50,300)
def book():
    p.book()
    p.status()
def cancel():
    p.cancel()
    p.status()
# time function
def time2():
    time1=time.strftime("%H:%M")
    date.config(text=time1)
    date.after(250,time2)
date=Label(box,font="times 20 ",bg="lightgreen")
date.place(x=1100,y=12)
Label(box,text="Time  - ",font="times 20 ",bg="lightgreen").place(x=1000,y=12)
time2()

# heading 

f3=Frame(box,width="500",height="300",bg="lightgreen").place(x=50,y=80)
Label(box,text="Booking Portal",font="times 30 bold underline",bg="lightgreen").place(x=460,y=9)
#  attributes  
Label(f3,text="Name",font="times 17 ",bg="lightgreen").place(x=100,y=100)
Label(f3,text="Age.",font="times 17 ",bg="lightgreen").place(x=100,y=140)
Label(f3,text="Gender",font="times 17 ",bg="lightgreen").place(x=100,y=180)
Label(f3,text="Phone No.",font="times 17 ",bg="lightgreen").place(x=100,y=220)
Label(f3,text="From",font="times 17 ",bg="lightgreen").place(x=100,y=260)
Label(f3,text="To",font="times 17 ",bg="lightgreen").place(x=100,y=300)
Label(f3,text="No. Of Seats",font="times 17 ",bg="lightgreen").place(x=100,y=340)

# variable define
namevalue=StringVar()
agevalue=StringVar()
gendervalue=StringVar()
phonevalue=StringVar()
fromvalue=StringVar()
tovalue=StringVar()
seatvalue=StringVar()

# attributes entry
name1=Entry(f3,textvariable=namevalue,bg="lightgreen").place(x=350,y=105)
age1=Entry(f3,textvariable=agevalue,bg="lightgreen").place(x=350,y=145)
gender1=Entry(f3,textvariable=gendervalue,bg="lightgreen").place(x=350,y=185)
phone1=Entry(f3,textvariable=phonevalue,bg="lightgreen").place(x=350,y=225)
from2=Entry(f3,textvariable=fromvalue,bg="lightgreen").place(x=350,y=265)
to1=Entry(f3,textvariable=tovalue,bg="lightgreen").place(x=350,y=305)
seat1=Entry(f3,textvariable=seatvalue,bg="lightgreen").place(x=350,y=345)

# button 
Button(box,text="Book Ticket",command=book,relief=SUNKEN,padx=15,pady=5,bg="lightgreen",font="times 15 bold").place(x=50,y=380)

# Ticket cancel
f2=Frame(box,width="500",height="100",relief=SUNKEN,bg="lightgreen").place(x=50,y=450)
Label(f2,text="Ticket NO.",font="times 15",bg="lightgreen").place(x=100,y=460)
Label(f2,text="Name",font="times 15",bg="lightgreen").place(x=100,y=500)
Entry(f2,textvariable=namevalue,bg="lightgreen").place(x=350,y=500)
Entry(f2,textvariable=namevalue,bg="lightgreen").place(x=350,y=460)
Button(f2,text="Cancel Ticket",command=cancel,relief=SUNKEN,padx=15,pady=5,bg="lightgreen",font="times 15 bold").place(x=50,y=550)



# Exit button
Button(box,text="Exit",command=exit,relief=SUNKEN,padx=15,pady=5,bg="lightgreen",font="times 15 bold").place(x=462,y=550)
lg.pack(fill=BOTH,expand=YES,padx=8,pady=8)
box.mainloop() 
