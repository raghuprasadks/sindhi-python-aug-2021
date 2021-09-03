"""
Dictionary - key value pair
{Key1:value1,key2:value2}
key should be unique in dictionary
it does maintain the insertion order
hence you cannot use the indexes
"""
teledict={"raghu":9845547471,"ravi":84848448,"jyothi":93939399}
print(" teledict ",teledict)
print(" teledict-datatype ",type(teledict))
#teledict[0]
print("value associated with key raghu" ,teledict['raghu'])
'''
updating value
'''
teledict["ravi"]=8888888888
print('after update ',teledict)
del teledict["ravi"]
print('after deletion ',teledict)
'''
Only print keys
'''
print ("only print keys" ,teledict.keys())
'''
Only print  values
'''
print ("only print values" ,teledict.values())
for k,v in teledict.items():
    print("key = ",k, " value = ",v)
'''
creation of dynamic dictionary name and aadhar
'''
aadhardict={}
noofele= int(input("enter no of records to add"))
for i in range(noofele):
    name=input("enter name")
    aadhar=input("enter aadhar")
    aadhardict[name]=aadhar
print("aadhar dict ",aadhardict)
    





