import sqlite3

# creating the items table
def create_table():
    #connet to database & create cursur
    conn = sqlite3.connect("item.db")
    c = conn.cursor()

    c.execute("""CREATE TABLE items(
        Item    TEXT,
        weight  INT, 
        value   INT
    )""")

    # commit and close the connetion to db
    conn.commit()
    conn.close()

# querry DB and show all records
def show_all():
    #connet to database & create cursur
    conn = sqlite3.connect("item.db")
    c = conn.cursor()

    c.execute("SELECT rowid,* FROM items")
    items = c.fetchall()
    for item in items:
        print(item)

    # commit and close the connetion to db
    # conn.commit()
    conn.close()

# add a new record to the table
def add_one(name: str, weight: int, value: int):
    #connet to database & create cursur
    conn = sqlite3.connect("item.db")
    c = conn.cursor()

    c.execute("INSERT INTO items VALUES (?,?,?)", (name,weight,value))

    # commit and close the connetion to db
    conn.commit()
    conn.close()

# add multiple new records to the table
def add_many(list :list):
    #connet to database & create cursur
    conn = sqlite3.connect("item.db")
    c = conn.cursor()

    c.executemany("INSERT INTO items VALUES (?,?,?)", (list))

    # commit and close the connetion to db
    conn.commit()
    conn.close()

# delete a record from the table
def delete_one(id: int):
    #connet to database & create cursur
    conn = sqlite3.connect("item.db")
    c = conn.cursor()

    c.execute("DELETE FROM items WHERE rowid = (?)", str(id))

    # commit and close the connetion to db
    conn.commit()
    conn.close()

# delete/drop table
def drop_table():
    #connet to database & create cursur
    conn = sqlite3.connect("item.db")
    c = conn.cursor()

    c.execute("DROP TABLE items")

    # commit and close the connetion to db
    conn.commit()
    conn.close()