from tkinter import *
import sqlite3

root = Tk()
root.title("Welcome to Corona Dashboard")
root.geometry('600x400')

statename = Label(root, text = "Enter State")
statename.grid(column=0,row=0)
statetxt = Entry(root, width=50)
statetxt.grid(column =1, row =0)

total = Label(root, text = "Enter total cases")
total.grid(column=0,row=1)
totaltxt = Entry(root, width=50)
totaltxt.grid(column =1, row =1)

active = Label(root, text = "Enter active cases")
active.grid(column=0,row=2)
activetxt = Entry(root, width=50)
activetxt.grid(column =1, row =2)

recovered = Label(root, text = "Enter recovered cases")
recovered.grid(column=0,row=3)
recoveredtxt = Entry(root, width=50)
recoveredtxt.grid(column =1, row =3)

death = Label(root, text = "Enter death cases")
death.grid(column=0,row=4)
deathtxt = Entry(root, width=50)
deathtxt.grid(column =1, row =4)

lbl = Label(root, text = " ")
lbl.grid(column=1,row=7)
# adding Entry Field

# function to display user text when
# button is clicked


def clicked():
    state = statetxt.get()
    total = int(totaltxt.get())
    active = int(activetxt.get())
    recovered = int(recoveredtxt.get())
    death = int(deathtxt.get())
    res="State : ",state, " Total : ",total," Active :",active," Recovered ",recovered, " Death : ",death
    lbl.configure(text = res)
    connection = sqlite3.connect("corona.db")
    connection.execute("insert into corona values ('%s','%d','%d','%d','%d')"  %(state,total,active,recovered,death))
    connection.commit()
    statetxt.delete(0, END)
    totaltxt.delete(0, END)
    activetxt.delete(0, END)
    recoveredtxt.delete(0, END)
    deathtxt.delete(0, END)
    
# button widget with red color text inside
btn = Button(root, text = "save" ,
			fg = "red", command=clicked)
# Set Button Grid
btn.grid(column=1, row=5)
# Execute Tkinter
root.mainloop()
