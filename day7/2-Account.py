"""
Account
Attributes - name,email,mobile,address,idproof
accountnumber
functionality - 
deposit - actno,amount
withdraw - actno,amount
checkBalance - actno
"""
import random
class Account():
    name=''
    email=''
    mobile=0
    address=''
    idprooof=''
    balance=0
    actno=0
    def openAccount(self,name,email,mobile,address,idproof):
        self.name = name
        self.email=email
        self.mobile = mobile
        self.address = address
        self.idproof = idproof
        self.actno = random.randint(1,100)
        return self.actno
    def deposit(self,actno,depamout):
        self.balance = self.balance + depamout
        return self.balance
    def withdraw(self,actno,withdrawamout):
        self.balance = self.balance -withdrawamout
        return self.balance
    def checkBal(self,actno):
        return self.balance
    def accountDetails(self):
        return "Name ",self.name," Balance : ",self.balance

act1 = Account()
actno = act1.openAccount("Raghu","raghu@gmail.com",9845547471,"1094,MCECHS Layout,Jakkuru,Bengaluru",2929292929)
print("Account number of Raghu ",actno)
bal = act1.deposit(actno,10000)
print("Balance after initial deposit ",bal)
bal = act1.deposit(actno,20000)
print("Balance after second deposit ",bal)
bal = act1.withdraw(actno,5000)
print("Balance after withdraw of 5k ",bal)
actdetails = act1.accountDetails()
print("Account details of raghu ",actdetails)
act2 = Account()
actno = act2.openAccount("Jatin","jatin@gmail.com",9845547471,"1094,MCECHS Layout,Jakkuru,Bengaluru",2929292929)
print("Account number of jatin ",actno)
bal = act2.deposit(actno,60000)
act3 = Account()
actno = act3.openAccount("Gagan","gagan@gmail.com",9845547471,"1094,MCECHS Layout,Jakkuru,Bengaluru",2929292929)
print("Account number of Gagan ",actno)
bal = act2.deposit(actno,80000)
'''
Account comparision - find the person with highest balance
'''
actlist=[]
actlist.append(act1)
actlist.append(act2)
actlist.append(act3)
maxbal=0
actwithmaxbal=''
for i in actlist:
    currbal = i.balance
    if (currbal > maxbal):
        maxbal=currbal
        actwithmaxbal = i.name
print("Person with max deposit ",actwithmaxbal)
print("max deposit ",maxbal)







    
    
    


