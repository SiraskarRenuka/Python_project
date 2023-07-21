# contact book using tkinter 
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.geometry('550x330')
root.resizable(0, 0)
root.title('CONTACT BOOK')
root.config(bg='pink')
contactList = [
['Renuka Siraskar', '9378654321'],
['Salman Khan', '9172658282'],
['Virat Kolhi', '8600530930'],
['Sha rukh Khan', '8600340180'],
['Amitab bacchan', '8600563423'],
['Akshay Kumar', '7722441234'],
['Varun Dhawan','9542973158'],
['Katrina Kaif','8576129463'],
['Shahid Kapoor','7794685135'],
['Deepika Padukone','9999954682'],
['Alia Bhatt','9458751236'],
['Ajay Devgn','8675945621'],
['Aamir Khan','8595754565'],
['MC Stan','9875546201'],
]
def addContact():
    name = name_entry.get()
    number = number_entry.get()
    if name and number:
        contactList.append([name, number])
        selectSet()
        name_entry.delete(0, tk.END)
        number_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Please enter both name and phone number.")
def deleteContact():
    if not contactList:
        return
    try:
        index = Selected()
        del contactList[index]
        selectSet()
    except IndexError:
        messagebox.showwarning("Error", "Please select a contact to delete.")
def viewContact():
    try:
        name, phone = contactList[Selected()]
        name_entry.delete(0, tk.END)
        name_entry.insert(0, name)
        number_entry.delete(0, tk.END)
        number_entry.insert(0, phone)
    except IndexError:
        messagebox.showwarning("Error", "Please select a contact to view.")
def exitApp():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        root.destroy()
def selectSet():
    contactList.sort()
    select.delete(0, tk.END)
    for name, phone in contactList:
        select.insert(tk.END, name)
def Selected():
    try:
        return int(select.curselection()[0])
    except IndexError:
        return -1
def clearSearchBox():
    name_entry.delete(0, tk.END)
    number_entry.delete(0, tk.END)

frame = tk.Frame(root)
frame.pack(side=tk.RIGHT)
name_label = tk.Label(root, text='CONTACT LIST', font=("calibri", 13, "bold"), bg="white")
name_label.place(x=420, y=30)
scroll = tk.Scrollbar(frame, orient=tk.VERTICAL)
select = tk.Listbox(frame, yscrollcommand=scroll.set, height=10)
scroll.config(command=select.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
select.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
name_label = tk.Label(root, text='NAME :-', font=("calibri", 12, "bold", 'underline'), bg='pink')
name_label.place(x=30, y=20)
name_entry = tk.Entry(root)
name_entry.place(x=130, y=20)
number_label = tk.Label(root, text='PHONE N0. :-', font=("calibri", 12, "bold", 'underline'), bg='pink')
number_label.place(x=30, y=70)
number_entry = tk.Entry(root)
number_entry.place(x=130, y=70)
name_label = tk.Label(root, text='MODIFY YOUR CONTACT LIST HERE: ', font=("calibri", 12, "bold"), bg="white")
name_label.place(x=30, y=120)
add_button = tk.Button(root, text="ADD CONTACT", font=("calibri", 10), command=addContact)
add_button.place(x=30, y=160)
delete_button = tk.Button(root, text="DELETE CONTACT", font=("calibri", 10), command=deleteContact)
delete_button.place(x=30, y=200)
view_button = tk.Button(root, text="VIEW CONTACT", font=("calibri", 10), command=viewContact)
view_button.place(x=30, y=240)
clear_button = tk.Button(root, text="CLEAR", font=("calibri", 10), command=clearSearchBox)
clear_button.place(x=30, y=280)
exit_button = tk.Button(root, text="EXIT", font=("calibri", 11, "bold"), bg='red', command=exitApp)
exit_button.place(x=250, y=280)
selectSet()
root.mainloop()
