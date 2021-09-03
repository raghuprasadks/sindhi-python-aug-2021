"""
1. create a dynamic dictionary of stocks
stocks={"companyname":["date","openingbalance","closingbalance","amounttraded"]}
2. Find out the company who has traded the most
3. Find the company where changes is maximum
4. Find the stock details of a specific company

stocks={
"infy":['27-08-2021',3000,3500,3939393993],
"wipro":['27-08-2021',2000,2300,394393993],
"hcl":['27-08-2021',1200,2200,494393993]
}
"""
stocks={
"infy":['27-08-2021',3000,3500,3939393993],
"wipro":['27-08-2021',2000,2300,394393993],
"hcl":['27-08-2021',1200,2200,494393993]
}
print("stocks ",stocks)
'''
2. Find out the company which has traded the most
'''
maxtradedamt=0
maxtradedcompany=''
for k,v in stocks.items():
    print("key ",k," value ",v)
    if (v[3]>maxtradedamt):
        maxtradedamt=v[3]
        maxtradedcompany=k
print("maximum traded amount ",maxtradedamt)
print("maximum traded company ",maxtradedcompany)
        
