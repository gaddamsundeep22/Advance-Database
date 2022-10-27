import sqlite3

# DB-API spec for talking to relational databases in Python

connection = sqlite3.connect("shopping_list.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table list")
except:
    pass

cursor.execute("create table list (id integer primary key, description text)")

cursor.execute("insert into list (description) values ('Sundeep')")
cursor.execute("insert into list (description) values ('Gaddam')")
cursor.execute("insert into list (description) values ('Rohith')")
cursor.execute("insert into list (description) values ('Vishal')")
cursor.execute("insert into list (description) values ('Ganesh')")

connection.commit()
connection.close()

print("done.")