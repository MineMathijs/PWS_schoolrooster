import sqlite3

conn = sqlite3.connect('test.db')

c = conn.cursor()

#insert row
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

#save changes
conn.commit()

conn.close()