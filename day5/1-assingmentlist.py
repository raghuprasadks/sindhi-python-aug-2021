# -*- coding: utf-8 -*-
"""
given a list of marks
marks = [20,25,11,24,16]
a.Find the total of marks
b. Find the maximum marks
c. Find the minimum marks
d. Find the average marks
not using built-in functions 
"""
marks = [20,25,11,24,16]
total = sum(marks)
print('total ',total)
maximum = max(marks)
print('maximum ',maximum)
minimum = min(marks)
print('minimum ',minimum)
avg = total/len(marks)
print('Average ',avg)

total = 0
maximum = marks[0]
minimum = marks[0]
counter = 0
for i in marks:
    total = total +i
    
    if (i>maximum):
        maximum = i
    if (i<minimum):
        minimum = i
    counter = counter +1
    #total += i
print("total ",total)
print("maximum ",maximum)
print("minimum ",minimum)
average = total/counter
print("average ",average)





