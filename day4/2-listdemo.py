# -*- coding: utf-8 -*-
"""
list - heterogeneous elements
"""
dummylist = [1,'two','three',4,5]
'''
looping
'''
for i in dummylist:
    print(i)

nooffriends=int(input("Enter no of friends"))
friendslist=[]
for i in range(nooffriends):
    name=input("Enter name")
    friendslist.append(name)
print("friends to be invited ",friendslist)
'''
built-in functions
'''
marks = [20,19,16,12,25]
print('maximum ',max(marks))
print('minimum ',min(marks))
print('total ',sum(marks))
print("average ",sum(marks)/len(marks))
'''
corona dashboard
'''
coronadashboard=[]
title=["state name","total","active","recovered","death"]
karnataka=["Karnataka",100000,20000,70000,10000]
kerala=["Kerala",200000,30000,140000,30000]
coronadashboard.append(title)
coronadashboard.append(karnataka)
coronadashboard.append(kerala)

print("corona dashboard ",coronadashboard)










