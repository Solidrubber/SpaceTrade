import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

#cursor.execute("INSERT INTO users VALUES(1,'solid', 'hasenfurz')")


create_table = "CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_table)

#cursor.execute("INSERT INTO items VALUES (1,'test', 10.99)")


create_table = "CREATE TABLE IF NOT EXISTS solarsystems(id INTEGER PRIMARY KEY, name text, px int, py int)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS ships(id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_table)



connection.commit()

connection.close()
