"""
List - 
Dynamic array
It allows duplicate values
It maintains the order of insertion
Elements can be accessed using index
"""
runs =[10,40,50,60]
print('runs -list ',runs)
print('runs -list - data type ',type(runs))
#<class 'list'>
print("list length ",len(runs))
'''
Adding an element
'''
runs.append(35)
print("after append ",runs)
'''
update an existing element
'''
runs[0]=15
print("after update ",runs)
'''
delete
'''
del runs[1]
print('after deletion ',runs)
'''
delete the list
'''
#del runs
#print('after deletion --',runs)
'''
find element at index 2
'''
print('element at index 2 ',runs[2])










