# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 17:35:18 2021

@author: lenovo
"""
import sqlite3
conn = sqlite3.connect('olympicsdb.db')
conn.execute('''
insert into olympics values ('tokiyo',2020,'usa',40,35,45,120)
    ''')
conn.execute('''
insert into olympics values ('tokiyo',2020,'china',35,35,45,115)
    ''')
conn.execute('''
insert into olympics values ('tokiyo',2020,'japan',30,35,45,110)
    ''')
conn.execute('''
insert into olympics values ('tokiyo',2020,'india',1,2,4,7)
    ''')
conn.commit();
print('data saved successfully')
conn.close()
