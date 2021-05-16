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

create_table = "CREATE TABLE IF NOT EXISTS planets(id INTEGER PRIMARY KEY, name text, px int, py int, solarsystemid INTEGER NOT NULL, FOREIGN KEY(solarsystemid) REFERENCES solarsystem(id))"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS ships(id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS moons(id INTEGER PRIMARY KEY, name text, amountRes real,planetid INTEGER NOT NULL, FOREIGN KEY(planetid) REFERENCES planet(id))"
cursor.execute(create_table)




connection.commit()

connection.close()
