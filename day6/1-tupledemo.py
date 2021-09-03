"""
Tuple - constant list
you cannot modify, you cannot add
days in a week
months in a year
items which are unique
"""
days=("Mon","Tue","Wed")
print("days ",days)
print("days-type ",type(days))
'''
you cannot perform following operations
append
modify
delete an element
'''
days.append("Thu")
'''
AttributeError: 'tuple' object has no attribute 'append'
'''
days[0]="Monday"
'''
TypeError: 'tuple' object does not support item assignment
'''
del days[0]
'''
TypeError: 'tuple' object doesn't support item deletion
'''
'''
following operations are allowed
'''
for i in days:
    print(i)
part = days[0:2]
print("slicing ",part)









