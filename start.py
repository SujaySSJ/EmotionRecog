#!/usr/bin/python
from Tkinter import *
import tkMessageBox
import os
top=Tk()

# def helloCallBack():
#     os.system('python captureVideo.py')

# B=Tkinter.Button(top,text="Video Capture",command= helloCallBack)
#B.pack()va
var=StringVar()
var2=StringVar()
label=Label(top,textvariable=var,relief=RAISED,width='200',fg='red',bd=0)
var.set("Facial Expression recognition system")
label.config(font=("Comic Sans MS", 44))


label2=Label(top,textvariable=var2,relief=RAISED,width='200',fg='black',justify='left',bd=0)
var2.set("Instructions\n\n")
label2.config(font=("Comic Sans MS", 20))

var3=StringVar()
string="1.Our system recognizes your emotions from your face....Obviously ..... : /..so try not to hide your face and don't be shy :))\n\n2.First we will record you and judge your emotions out of your face...:))\n\n3. Then we would provide you a statistical data of the emotions.\n\n4. Be as natural and honest as possible(if you are!!) and don't forget you are being monitored...muhahahahahaha..."
label3=Label(top,textvariable=var3,relief=RAISED,width='200',fg='black',justify='left',bd=0)
var3.set(string)
label3.config(font=("Comic Sans MS", 16))
label.pack()
label2.pack()
label3.pack()
def helloCallBack():
    os.system('python captureVideo.py')
B=Button(top,text="Click to start your video Caputre->",command= helloCallBack,width=50,fg='red',bd=5)
B.config(font=("Comic Sans MS", 16))
B.pack()
top.mainloop()