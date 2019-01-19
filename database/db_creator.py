import sqlite3


connect=sqlite3.connect('data.db')
cursor=connect.cursor()
createtable="CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY  KEY ,username tetx, password tetx)"
cursor.execute(createtable)

create_table="CREATE TABLE IF NOT EXISTS items (name tetx, price real)"
cursor.execute(create_table)

insertitm="INSERT INTO items VALUES('test',9.99 )"
cursor.execute(insertitm)


user=(1,'josein','asdf')
insert="INSERT INTO users VALUES(?,?,?)"
cursor.execute(insert,user)

users=(2,'adolfo', 'sadf')
userrrr=(3,'fideli', 'wdv')
cursor.execute(insert, userrrr)
cursor.execute(insert, users)

select="SELECT * FROM users"
for item in cursor.execute(select) :
    print(item)

connect.commit()
connect.close()