import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os,time
import tkinter
tkinter.Tk().bell()

def createWidgets():
    label1=Label(root,text='Enter the time hare in hh:mm -')
    label1.grid(row=0,column=0,padx=5,pady=5)

    global entry1
    entry1 = Entry(root,width=5)
    entry1.grid(row=0,column=1)


    label2=Label(root,text='Enter the message of alarm:')
    label2.grid(row=0,column=0,padx=5,pady=5) 

    global entry2
    entry2 = Entry(root,width=5)
    entry2.grid(row=0,column=1)


root=tk.Tk()
root.title("Alarm clock")
root.geometry("")


createWidgets()

root.mainloop()



