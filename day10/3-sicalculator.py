# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 10:53:45 2021

@author: lenovo
"""


from tkinter import *

class SICalculator():
    def __init__(self,root):
        self.f = Frame(root,height=350, width = 500)
        #self.f.propagate(0)
        self.f.pack()
        
        # labels
        self.l1 = Label(text='Principal')
        self.l2 = Label(text='Rate')
        self.l3 = Label(text='Time')
        
        self.l1.place(x=50,y=100)
        self.l2.place(x=50,y=150)
        self.l3.place(x=50,y=200)
        
        #Entry for user name
        
        self.e1 = Entry(self.f,width = 25,fg='blue',bg='yellow',font=('Arial',14))
        
        self.e2 = Entry(self.f,width = 25,fg='blue',bg='yellow',font=('Arial',14))
        
        self.e3 = Entry(self.f,width = 25,fg='blue',bg='yellow',font=('Arial',14))
        
        self.e1.place(x=150,y=100)
        self.e2.place(x=150,y=150)
        self.e3.place(x=150,y=200)
        self.e3.bind("<Return>",self.display)
        
    def display(self,event):
        str1 = self.e1.get()
        str2 = self.e2.get()
        str3 = self.e3.get()
        interest = float(str1)*float(str2)*float(str3)/100
        strinterest = str(interest)
        # display the values uisng labels
        lbl1 = Label(text='Interest is : '+strinterest).place(x=150,y=300)
        
root = Tk()
me = SICalculator(root)
root.mainloop()

