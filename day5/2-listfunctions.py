"""
https://docs.python.org/3/tutorial/datastructures.html
"""
'''
Slicing
'''
marks = [10,24,25,23,12]
markspart1 = marks[0:3]
markspart2 = marks[2:5]
print('sliced list:markspart1 ',markspart1)
print('sliced list:markspart2 ',markspart2)
lastele = marks[-1]
print("last element ",lastele)
elements =marks[::1]
print('all elements ',elements)
altelements =marks[::2]
print('alt elements ',altelements)
index25 = marks.index(25)
print(index25)
print(marks.index(100))
'''
Sorting in ascending order
'''
marks.sort()
print(marks)
'''
Sorting in descending order
'''
marks.sort(reverse=True)
print(marks)
'''
insert element at 2 position
'''
print('existing list ',marks)
marks.insert(2,100)
print('marks after insertion ',marks)
runs=[20,3,4,20,3,5]
print('count ',runs.count(3))

