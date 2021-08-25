'''
Function without parameter
'''
def greet():
    print('Good morning')
greet()
'''
Function with a parameter
'''
def greet(name):
    print(name, ' Good morning')
greet('ravi')
name = input("Enter your name")
greet(name)
'''
Function with multiple parameters
'''
def simpleInterest(p,r,t):
    return p*r*t/100
si= simpleInterest(10000,4,1)
print('simple interest is ',si)
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
print('Use me to calculate')
oper = input("enter operation - A,S,M,D")
n1 = int(input("enter first number"))
n2 = int(input("enter second number"))
result = 0
if (oper=='A'):
    result = add(n1,n2)
if (oper=='S'):
    result = subtract(n1,n2)
print('Result of ',oper,' is ',result)









