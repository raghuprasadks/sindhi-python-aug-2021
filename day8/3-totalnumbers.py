file = open('india.txt','r')
lines = file.readlines()
total = 0
for line in lines:
    #print(line)
    wordlist = line.split()
    for word in wordlist:
        replacedword = word.replace('.','')
        if (replacedword.isdigit()):
            total = total +int(replacedword)            
            #print(replacedword)
file.close()

print('total ',total)