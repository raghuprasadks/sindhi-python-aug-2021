# -*- coding: utf-8 -*-
"""
Assignment
Calculation of Electricity bill by using a function

units consumed upto 100 - 1 rs per unit
units consumed between 101 to 200 - 2 rs per unit
units consumed between 201 to 300 - 3 rs per unit
units consumed above 300 is 5 rs per unit

calculation - cumulative: 
50 units - 50 X 1 = 50
150 units - 
first 100 - 100 X 1
next 50 - 50 X 2 
total - 200
"""

def calculateEBill(units):
    amt=0
    if (units <=100):
        amt = units *1
    elif (units >100 and units <=200):
        amt = (units -100)*2 + 100 *1
    elif (units >200 and units <=300):
        amt=(units-200)*3 + 100 * 1 + 100 *2
    elif (units >300):
        amt=(units-300)*5 + 100 * 1 + 100 *2+100*3
    return amt

units=int(input("Enter units consumed"))
amt_to_pay = calculateEBill(units)
print("Your bill amount is ",amt_to_pay, " for units consumed ",units)











