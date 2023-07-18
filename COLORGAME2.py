#Colour game in python 

from tkinter import *
import random
colours=['Red','Blue','Green',"Pink",'Black','Yellow','Orange','White','Purple','Brown']
score=0
timeleft=30
def startGame(event):
    if timeleft==30:
        countDown()

    nextColour()
root=Tk()
root.title("COLOURGAME")
root.geometry("400x300")
scoreLabel=Label(root,text=".....press Enter key to start game...",font=('Times New Roman',15))
scoreLabel.pack()
instructions=Label(root,text="Type the colour of the text",font=('Times New Roman',15))
instructions.pack()
timeLabel=Label(root,text="Time Left:"+str(timeleft),font=('Times New Roman',15))
timeLabel.pack()
label=Label(root,font=('Times New Roman',60))
label.pack()

e=Entry(root,font=('Times New Roman',15))
root.bind("<Return>",startGame)
e.pack()
e.focus_set()

def nextColour():
    global score
    global timeleft
    if timeleft>0:
        e.focus_set()
        if e.get().lower()==colours[1].lower():
            score+=1
        e.delete(0,END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]),text=str(colours[0]))
        scoreLabel.config(text="Score:"+str(score))
def countDown():
    global timeleft
    if timeleft>0:
        timeleft -=1
        timeLabel.config(text="Time Left :"+str(timeleft))
        timeLabel.after(1000,countDown)
mainloop()


