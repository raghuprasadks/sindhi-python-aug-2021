from tkinter import *

class corona():
    def __init__(self,root):
        self.f = Frame(root,height=600, width = 500)
        #self.f.propagate(0)
        self.f.pack()
        
        # labels
        self.l1 = Label(text='state')
        self.l2 = Label(text='total')
        self.l3 = Label(text='active')
        self.l4 = Label(text='recovered')
        self.l5 = Label(text='death')
        
        
        self.l1.place(x=50,y=100)
        self.l2.place(x=50,y=150)
        self.l3.place(x=50,y=200)
        self.l4.place(x=50,y=250)
        self.l5.place(x=50,y=300)
        
        
        #Entry for user name
        
        self.e1 = Entry(self.f,width = 25,fg='blue',bg='yellow',font=('Arial',14))
        
        self.e2 = Entry(self.f,width = 25,fg='blue',bg='yellow',font=('Arial',14))
        
        self.e3 = Entry(self.f,width = 25,fg='blue',bg='yellow',font=('Arial',14))
        
        self.e4 = Entry(self.f,width = 25,fg='blue',bg='yellow',font=('Arial',14))
        
        self.e5 = Entry(self.f,width = 25,fg='blue',bg='yellow',font=('Arial',14))
        
        
        self.e1.place(x=150,y=100)
        self.e2.place(x=150,y=150)
        self.e3.place(x=150,y=200)
        self.e4.place(x=150,y=250)
        self.e5.place(x=150,y=300)
        
        self.e5.bind("<Return>",self.display)
        
    def display(self,event):
        str1 = self.e1.get()
        str2 = self.e2.get()
        str3 = self.e3.get()
        str4 = self.e4.get()
        str5 = self.e5.get()
        
        # display the values uisng labels
        lbl1 = Label(text='Your state is : '+str1).place(x=150,y=400)
        lb12 = Label(text='Your total is : '+str2).place(x=150,y=420)
        lbl3 = Label(text='Your active is : '+str3).place(x=150,y=440)
        lbl4 = Label(text='Your recovered is : '+str4).place(x=150,y=460)
        lb15 = Label(text='Your death is :  '+str5).place(x=150,y=480)
        
        
        
root = Tk()
me = corona(root)
root.mainloop()