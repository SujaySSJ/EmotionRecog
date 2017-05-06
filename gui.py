#!/usr/bin/python
import sys
import os
import Tkinter
import tkMessageBox
top=Tkinter.Tk()

def helloCallBack():
    os.system('python captureVideo.py')

B=Tkinter.Button(top,text="Video Capture",command= helloCallBack)
B.pack()
top.mainloop()