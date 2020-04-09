# -*- coding: utf-8 -*-
from Tkinter import *
import tkFont

win=Tk()


myFont =tkFont.Font(family= 'Helvetica', size=24, weight='bold')

def redFunc(red):
    print("red changed:" + red)
def greenFunc(green):
    print("green changed:" + green)
    frissg(green,22)
def blueFunc(blue):
    print("blue changed:" + blue)
    
def button1_pressed():
    print('Button1 pressed')
  


win.title('Tkinter example')
win.geometry('1024x600')
win.config(background = "#3d3d3d")


button1 = Button(win,text = "Button1 text", font = myFont, command =button1_pressed, height =1, width =10, bg="#696969",activebackground="#696969", fg="white", activeforeground= "white", borderwidth=0)
button1.grid(row=0,column=0, padx=10, pady=2)


red=Scale(win,orient=HORIZONTAL, length=280, width=50, sliderlength=60, from_=0, to=255, tickinterval=50, command=redFunc, troughcolor ="#f02921", highlightcolor="#696969", bg="#696969", fg="white")
red.grid(row=1,column=0,padx=10,pady=10)
green=Scale(win,orient=HORIZONTAL, length=280, width=50, sliderlength=60, from_=0, to=255, tickinterval=50, command=greenFunc, troughcolor ="#29cc29", highlightcolor="#696969", bg="#696969", fg="white")
green.grid(row=2,column=0,padx=10,pady=10)
blue=Scale(win,orient=HORIZONTAL, length=280, width=50, sliderlength=60, from_=0, to=255, tickinterval=50, command=blueFunc, troughcolor ="#006bc6", highlightcolor="#696969", bg="#696969", fg="white")
blue.grid(row=3,column=0,padx=10,pady=10)


#rightFrame =Frame(win, width=200, height=500, bg="#3d3d3d")
#rightFrame.grid(row=0, column=1, padx=10, pady=2)

#circleCanvas=Canvas(rightFrame, width= 180, height=200, bg="#3d3d3d", bd=0, highlightbackground="#3d3d3d")
#circleCanvas.grid(row=0,column=0,padx=10,pady=2)
#circleCanvas.create_oval(0,0,180,200, width=0, fill='#18357b')
#label1=Label(rightFrame, text="20℃", fg="white", bg="#18357b", font=("Helvetica)", 36))
#label1.grid(row=0,column=0,padx=10,pady=2)
#imagex=PhotoImage(file='example.jpg')


mainloop()


# Documentation: https://docs.python.org/3/library/tkinter.html 


    
