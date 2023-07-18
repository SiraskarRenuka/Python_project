#This code calculate a SGPA from subject credits

from tkinter import *
w = Tk()
w.title("MARKSHEET")
w.resizable(0,0)
w.geometry("700x250")

e1 = Entry(w)
e2 = Entry(w)
e3 = Entry(w)
e4 = Entry(w)
e5 = Entry(w)
e6 = Entry(w)
e7 = Entry(w)

# function to display the total subject
# credits total credits and SGPA according
# to grades entered
def display():
	tot = 0
	if e4.get() == "A":
		# grid method is used for placing
		# the widgets at respective positions
		# in table like structure .
		Label(w, text="40").grid(row=3, column=4)
		tot += 40

	# 9*number of subject credits give
	# total credits for grade B
	if e4.get() == "B":
		Label(w, text="36").grid(row=3, column=4)
		tot += 36

	# 8*number of subject credits give
	# total credits for grade C
	if e4.get() == "C":
		Label(w, text="32").grid(row=3, column=4)
		tot += 32

	# 7*number of subject credits
	# give total credits for grade D
	if e4.get() == "D":
		Label(w, text="28").grid(row=3, column=4)
		tot += 28

	# 6*number of subject credits give
	# total credits for grade P
	if e4.get() == "P":
		Label(w, text="24").grid(row=3, column=4)
		tot += 24

	# 0*number of subject credits give
	# total credits for grade F
	if e4.get() == "F":
		Label(w, text="0").grid(row=3, column=4)
		tot += 0

	# Similarly doing with other objects
	if e5.get() == "A":
		Label(w, text="40").grid(row=4, column=4)
		tot += 40
	if e5.get() == "B":
		Label(w, text="36").grid(row=4, column=4)
		tot += 36
	if e5.get() == "C":
		Label(w, text="32").grid(row=4, column=4)
		tot += 32
	if e5.get() == "D":
		Label(w, text="28").grid(row=4, column=4)
		tot += 28
	if e5.get() == "P":
		Label(w, text="28").grid(row=4, column=4)
		tot += 24
	if e5.get() == "F":
		Label(w, text="0").grid(row=4, column=4)
		tot += 0

	if e6.get() == "A":
		Label(w, text="30").grid(row=5, column=4)
		tot += 30
	if e6.get() == "B":
		Label(w, text="27").grid(row=5, column=4)
		tot += 27
	if e6.get() == "C":
		Label(w, text="24").grid(row=5, column=4)
		tot += 24
	if e6.get() == "D":
		Label(w, text="21").grid(row=5, column=4)
		tot += 21
	if e6.get() == "P":
		Label(w, text="28").grid(row=5, column=4)
		tot += 24
	if e6.get() == "F":
		Label(w, text="0").grid(row=5, column=4)
		tot += 0

	if e7.get() == "A":
		Label(w, text="40").grid(row=6, column=4)
		tot += 40
	if e7.get() == "B":
		Label(w, text="36").grid(row=6, column=4)
		tot += 36
	if e7.get() == "C":
		Label(w, text="32").grid(row=6, column=4)
		tot += 32
	if e7.get() == "D":
		Label(w, text="28").grid(row=6, column=4)
		tot += 28
	if e7.get() == "P":
		Label(w, text="28").grid(row=6, column=4)
		tot += 24
	if e7.get() == "F":
		Label(w, text="0").grid(row=6, column=4)
		tot += 0

	# to display total credits
	Label(w, text=str(tot),font=("calibri",10,'bold')).grid(row=7, column=4)

	# to display SGPA
	Label(w, text=str(tot/15),font=("calibri",10,'bold')).grid(row=8, column=4)


# end of display function

# label to enter name
Label(w, text="Name",font=("calibri",10,'bold')).grid(row=0, column=0)

# label for registration number
Label(w, text="Reg.No",font=("calibri",10,'bold')).grid(row=0, column=3)

# label for roll Number
Label(w, text="Roll.No",font=("calibri",10,'bold')).grid(row=1, column=0)

# labels for serial numbers
Label(w, text="Sr.No",font=("calibri",10,'bold')).grid(row=2, column=0)
Label(w, text="1").grid(row=3, column=0)
Label(w, text="2").grid(row=4, column=0)
Label(w, text="3").grid(row=5, column=0)
Label(w, text="4").grid(row=6, column=0)


# labels for subject 
Label(w, text="Subject",font=("calibri",10,'bold')).grid(row=2, column=1)
Label(w, text="Python").grid(row=3, column=1)
Label(w, text="Android").grid(row=4, column=1)
Label(w, text="Java").grid(row=5, column=1)
Label(w, text="HTML").grid(row=6, column=1)


# label for grades
Label(w, text="Grade",font=("calibri",10,'bold')).grid(row=2, column=2)
e4.grid(row=3, column=2)
e5.grid(row=4, column=2)
e6.grid(row=5, column=2)
e7.grid(row=6, column=2)


# labels for subject credits
Label(w, text="Sub Credit",font=("calibri",10,'bold')).grid(row=2, column=3)
Label(w, text="4").grid(row=3, column=3)
Label(w, text="4").grid(row=4, column=3)
Label(w, text="3").grid(row=5, column=3)
Label(w, text="4").grid(row=6, column=3)

Label(w, text="Credit obtained",font=("calibri",10,'bold')).grid(row=2, column=4)

# taking entries of name, reg, roll number respectively
e1 = Entry(w)
e2 = Entry(w)
e3 = Entry(w)

# organizing them in the grid
e1.grid(row=0, column=1)
e2.grid(row=0, column=4)
e3.grid(row=1, column=1)

# button to display all the calculated credit scores and sgpa
button1 = Button(w, text="CALCULATE",font=("calibri",10,'bold'), bg="green",command=display)
button1.grid(row=8, column=1)

Label(w, text="Total credit",font=("calibri",10,'bold')).grid(row=7, column=3)
Label(w, text="SGPA",font=("calibri",10,'bold')).grid(row=8, column=3)

mainloop()
