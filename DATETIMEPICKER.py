from tkinter import *
from tkcalendar import *
root=Tk()
root.title('DATE TIME PICKER')
root.resizable(0,0)
root.geometry("500x400")

hour_string=StringVar()
min_string=StringVar()
sec_string=StringVar()
f=("Times New Roman",20)

fone=Frame(root)
ftwo=Frame(root)

fone.pack(pady=10)
ftwo.pack(pady=10)
cal=Calendar(fone,selectmode='day',year=2023,month=2,day=21)
cal.pack()

min=Spinbox(ftwo,from_=0,to=23,wrap=True,textvariable=min_string,width=2,state="readonly",font=f,justify=CENTER)
hour=Spinbox(ftwo,from_=0,to=59,wrap=True,textvariable=hour_string,width=2,font=f,justify=CENTER)
sec=Spinbox(ftwo,from_=0,to=59,wrap=True,textvariable=sec_string,width=2,font=f,justify=CENTER)

min.pack(side=LEFT,fill=X,expand=True)
hour.pack(side=LEFT,fill=X,expand=True)
sec.pack(side=LEFT,fill=X,expand=True)

def display_msg():
    date=cal.get_date()
    m=min.get()
    h=hour.get()
    s=sec.get()
    t=f"You Select :- DATE {date} AND TIME {m}:{h}:{s}."
    msg_display.config(text=t)

msg=Label(root,text="Hour Minute Second",font=("Times New Roman",12))
msg.pack(side=TOP)

action=Button(root,text="SELECT",padx=10,pady=10,command=display_msg)
action.pack(pady=10)

msg_display=Label(root,text=" ",font=("Times New Roman",12),fg="white",bg="black")
msg_display.pack(pady=10)

mainloop()





