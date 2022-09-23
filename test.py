import sqlite3
from venv import create

conn = sqlite3.connect('test.db')

c = conn.cursor()

#create table:
c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')