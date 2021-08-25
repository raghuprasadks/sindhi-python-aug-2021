"""
Assignment - 1

An ecommerce website published following
advertisement in a news paper.

Discount is calculated based on the amount of 
purchase
purchase amount <10000 - discount is 5 %
purchase amount >=10000 and <20000- discount is 10 %
purchase amount >=20000 and <30000- discount is 15 %
purchase amount >=30000  discount is 20 %
Additionally for prime customers additional 
discount is 5 %.
Write a program to calculate the discount and net
amount to be paid by getting 
user inputs of purchase amount and 
whether he/she is a prime customer
"""
'''
WITHOUT USING FUNCTION
'''

purchaseamt=int(input("Enter purchase amount"))
isPrime = input("Enter Y for prime N for Nonprime")

discount=0
netamount=0
discountpercentage=0
if(purchaseamt<10000):
    discountpercentage=.05
elif(purchaseamt>=10000 and purchaseamt<20000):
    discountpercentage=.1
if (isPrime=='Y'):
    discount=purchaseamt*discountpercentage+purchaseamt*.05
else:
    discount=purchaseamt*discountpercentage

netamount=purchaseamt-discount

print("Purchase amount = ",purchaseamt," discount = ",discount, "Net amount =",netamount)


'''
with function
'''
def discountCalculator(purchaseamt,isPrime):
    discount=0
    netamount=0
    discountpercentage=0
    if(purchaseamt<10000):
        discountpercentage=.05
    elif(purchaseamt>=10000 and purchaseamt<20000):
        discountpercentage=.1
    if (isPrime=='Y'):
        discount=purchaseamt*discountpercentage+purchaseamt*.05
    else:
        discount=purchaseamt*discountpercentage
    
    netamount=purchaseamt-discount
    
    return netamount,discount


netamt,discount = discountCalculator(purchaseamt,isPrime)
print("With functions : Purchase amount = ",purchaseamt," discount = ",discount, "Net amount =",netamt)


    

















