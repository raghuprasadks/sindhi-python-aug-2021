"""
olympic dictionary dynamically
{"usa":[38,40,40,118],"china":[40,40,40,120]}
"""
noofcountries = int(input("Number of countries"))
olympdict={}
for i in range(noofcountries):
    cname=input("Enter country")
    gold=int(input("Enter gold"))
    silver=int(input("Enter silver"))
    bronze=int(input("Enter bronze"))
    total = gold+silver+bronze
    olympdict[cname]=[gold,silver,bronze,total]
print("olympic medals dictionary ",olympdict)    


