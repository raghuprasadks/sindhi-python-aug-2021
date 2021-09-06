# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 17:35:18 2021

@author: lenovo

location	TEXT,
	year	INTEGER,
	country	TEXT,
	gold	INTEGER,
	silver	INTEGER,
	bronze	INTEGER,
	total	INTEGER
"""
import sqlite3
conn = sqlite3.connect('olympicsdb.db')
records = conn.execute(''' 
             update olympics set gold=41,total=121 where country='usa'
''')

conn.commit()

records = conn.execute(''' 
             select * from  olympics where country='usa'
''')

for record in records:
    #print(record)
    
    print ("location ",record[0],"year ",record[1]," country ",record[2]," gold ",record[3]," silver ",record[4]," bronze ",record[5]," total ",record[6])
conn.close()
