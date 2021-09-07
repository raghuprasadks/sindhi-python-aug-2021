# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 10:32:16 2021

@author: lenovo
"""

from tkinter import *
class MyEntry():
    def __init__(self,root):
        self.f = Frame(root,height=350, width = 500)
        self.f.pack()
        self.l1 = Label(text='Enter user name')
        self.l2 = Label(text='Enter password')
        self.l1.place(x=50,y=100)
        self.l2.place(x=50,y=150)
        #Entry for user name
        self.e1 = Entry(self.f,width = 25,fg='blue',bg='yellow',font=('Arial',14))
        self.e2 = Entry(self.f,width = 25,fg='blue',bg='yellow',font=('Arial',14),show='*')
        self.e1.place(x=150,y=100)
        self.e2.place(x=150,y=150)
        self.e2.bind("<Return>",self.display)
        
    def display(self,event):
        str1 = self.e1.get()
        str2 = self.e2.get()
        
        # display the values uisng labels
        lbl1 = Label(text='Your name is : '+str1).place(x=150,y=200)
        lb12 = Label(text='Your password is  '+str2).place(x=150,y=220)

root = Tk()
me = MyEntry(root)
root.mainloop()
