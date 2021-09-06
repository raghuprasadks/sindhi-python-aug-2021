info='''corona is a deadly virus.
corona is originated from wuhan,china.
corona infected many people across the globe.
'''
print('info ',info)
print('convert to upper ',info.upper())
print('convert to lower ',info.lower())
print('capitalize ',info.capitalize())
print('count of word corona ',info.count('corona'))
for i in info:
    print(i)
aftersplit = info.split()
print('after split ',aftersplit)
for word in aftersplit:
    print(word)
print('ends with ',info.endswith('globe.'))
'''
isdigit()
isalpha()
isdecimal()
index()
format()
strip()
'''
word=' 1947 '

print('is digit ',word.isdigit())
print('is alpha ',word.isalpha())
print('strip ',word.strip())
print('index ',info.index('originated'))

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
print('txt1 afer formatting ',txt1)
txt2 = "My name is {0}, I'm {1}".format("John",36)
print('txt2 afer formatting ',txt2)
txt3 = "My name is {}, I'm {}".format("John",36)
print('txt3 afer formatting ',txt3)




