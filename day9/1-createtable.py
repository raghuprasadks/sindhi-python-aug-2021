import sqlite3
conn = sqlite3.connect('olympicsdb.db')
conn.execute('''             
CREATE TABLE if not exists olympics (
	location	TEXT,
	year	INTEGER,
	country	TEXT,
	gold	INTEGER,
	silver	INTEGER,
	bronze	INTEGER,
	total	INTEGER
)
'''             
)
print('table created successfully')
conn.close()
