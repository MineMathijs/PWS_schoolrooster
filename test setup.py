import sqlite3
import random
import names

conn = sqlite3.connect("test2.db")

c = conn.cursor()

#c.execute("CREATE TABLE student(studentid int primary key, naam text, nederlands boolean, wiskunde boolean, engels boolean, informatica boolean)")

#c.execute("INSERT INTO student VALUES (0003,'MARK', TRUE, FALSE, TRUE, TRUE)")

c.execute("DELETE FROM student")

for i in range(1,20):
    naam = names.get_first_name()
    ned = random.getrandbits(1)
    wis = random.getrandbits(1)
    eng = random.getrandbits(1)
    inf = random.getrandbits(1)
    c.execute("INSERT INTO student VALUES("+ str(i) + ","+ str +"," + str(ned) + "," + str(wis) + "," + str(eng) + "," + str(inf) +  ")")

conn.commit()

conn.close()