'''
agenda
conditional statements
functions
assignments
'''
age = int(input("Enter your age"))
if (age>=18):
    print("You are eligible for vaccine")
else:
    print("You are not yet eligible for vaccine")
'''
marks >90 <=100 - A+
marks >80 <=90 - A
marks >70 <=80 - B+
'''
marks = int(input("Enter marks"))
if (marks >90 and marks <=100):
    print("A+")
elif(marks >80 and marks <=90):
    print("A")
elif(marks >70 and marks <=80):
    print("B+")
elif(marks >60 and marks <=70):
    print("B")
else:
    print("less than B")
    








