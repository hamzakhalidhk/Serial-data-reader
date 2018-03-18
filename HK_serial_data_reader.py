import serial
from tkinter import messagebox
import ttk
try:
    from tkinter import *
except:
    from tkinter import *
import datetime

import sqlite3
import time
import datetime
import random


def pro():
    messagebox.showinfo(title= "About Project", message="This is an AVR based realtime P/I/V monitoring system made by Haris Bin Ashraf")
    return
def dev():
    messagebox.showinfo(title= "About Developer", message="This is a python based software made by HK developers. Place an order at: itshamzakhalidhk@gmail.com")
    return
def ex():
    ex = messagebox.askyesno(title= "Quit", message="Are you Sure?")
    if ex >0:
        root.destroy()
        return
thing = ' '

class main:
    def __init__(self,root,ser):
        self.ser=ser
        self.root=root
        self.root.title("Monitor")
        self.root.geometry('700x600-30+30')
        self.root.resizable(width=False,height=False)
        self.canvas = Canvas(self.root, width=300, height=100)
        self.canvas.place(x=340,y=140)
        self.canvas1 = Canvas(self.root, width=300, height=100)
        self.canvas1.place(x=340, y=240)
        self.canvas2 = Canvas(self.root, width=300, height=100)
        self.canvas2.place(x=340, y=340)
        self.blackBox = self.canvas.create_rectangle(10,10,500,100,fill='black')
        self.s = StringVar()
        self.blackBox1 = self.canvas1.create_rectangle(10, 10, 500, 100, fill='black')
        self.blackBox2 = self.canvas2.create_rectangle(10, 10, 500, 100, fill='black')
        self.LABELh = Label(self.root, text='LIVE MONITORING', font=("Arial", "40"))
        self.LABELh.place(x=120,y=40)
        self.LABELx = Label(self.root, text='Voltage: ' ,font=("Verdana", "50"))
        self.LABELx.place(x=30,y=150)
        self.LABEL = Label(self.root,text='',textvariable = self.s, font=("Verdana","50"),bg='black', fg='lime')
        self.LABEL.place(x=350,y=150)
        self.s1 = StringVar()
        self.LABELy = Label(self.root, text='Current: ' ,font = ("Verdana", "50"))
        self.LABELy.place(x=30,y=250)
        self.LABEL1 = Label(self.root, text='', textvariable=self.s1, font=("Verdana", "50"),bg='black', fg='lime')
        self.LABEL1.place(x=350,y=250)
        self.s2 = StringVar()
        self.LABELz = Label(self.root, text='Load: ', font = ("Verdana", "50"))
        self.LABELz.place(x=130,y=350)
        self.LABEL2 = Label(self.root, text='', textvariable=self.s2, font=("Verdana", "50"),bg='black', fg='lime')
        self.LABEL2.place(x=350,y=350)

        self.root.after(60,self.min)

    def min(self):

        thing = self.ser.readline().decode('ascii')
        string = str(thing)
        i=0
        j=0
        k=0
        for i in range(37, len(string)):
            if string[i] == 'V':
                break
        v=string[36:i]
        for j in range(48, len(string)):
            if string[j] == 'A':
                break
        c= string[i + 11:j]
        for k in range(60, len(string)):
            if string[k] == 'W':
                break
        p=string[j + 8:k]
        self.s.set(" " + v + " V")
        self.s1.set(" " +c + " A")
        self.s2.set(" " +p + " W")
        self.root.after(60, self.min)

        print ("v= " + v)
        print("i= " + c)
        print("p= " + p)


        self.root.update()
        # Haris Bin Ashraf Data ---> Voltage: 128V Current: 128A Load: 128W

def stopServer():
    sure=messagebox.askyesno(title='Quit',message='Are you Sure?')
    if sure >0:
        root.destroy()
        return
def startServer():
    try:
        com = portNo.get()
        ser = serial.Serial(com, 9600, timeout=0)
        print('Serial port is open')
        main(root,ser)
        Button1.destroy()
        Button2 = Button(root, text='       Stop Server and Exit      ', command=stopServer, font=("Arial","14"))
        Button2.place(x=230, y=480)
    except:
        Labelerror = Label(root, text='Invalid Port or Error Reading', font=("Arial","14"),  fg='red')
        Labelerror.place(x=110, y=150)
    return

root = Tk()
portNo = StringVar()
root.geometry("500x250+50+50")
root.title('HK Serial Data Reader')
root.resizable(width=False,height=False)
Labelh=Label(root,text='Enter port Name. E.g: COM4',font=("Arial","14")).place(x=120,y=40)
entry1=Entry(root,textvariable=portNo).place(x=185,y=80)
Button1= Button(root,text='Start Server', command=startServer, font=("Arial","10") )
Button1.place(x=205,y=110)

#Menu
menubar=Menu(root)
optionsmenu = Menu(menubar, tearoff = 0)
optionsmenu.add_command(label="Project", command = pro)
optionsmenu.add_command(label="Developer", command = dev )
optionsmenu.add_command(label="Exit", command= ex)
optionsmenu.add_separator()
menubar.add_cascade(label="Options",menu=optionsmenu)
root.config(menu=menubar)

root.mainloop()