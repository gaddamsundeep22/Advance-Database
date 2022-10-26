import sqlite3
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
cursor.execute("insert into list (description) values ('Ganesh')")
cursor.execute("insert into list (description) values ('Vishal')")

connection.commit()
connection.close()

print("done.")