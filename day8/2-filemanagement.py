"""
File management
Modes 
w - write mode - existing content will be deleted
a - content gets added to the existing file
r - read content of a file
"""
file=open("olympics.txt","w")
file.write("Olympics 2020 was held in japan \n")
file.write("More than 170 countries participated in it")
file.close()

file=open("olympics.txt","w")
file.write("US came first followed by china \n")
file.close()

file=open("olympics.txt","a")
file.write("\n India performed well compared to previous olympics \n")
file.close()

file=open("olympics.txt","r")
info = file.read()
print(info)
file.close()

'''
reading line by line
'''
file=open("olympics.txt","r")
info = file.readlines()
for i in info:
    print(i)
file.close()





