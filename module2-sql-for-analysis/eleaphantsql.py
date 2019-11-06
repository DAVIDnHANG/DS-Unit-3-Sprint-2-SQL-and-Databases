import psycopg2
#read docs use help()
#help(psycopg2.connect)


#setting up for psycopy2.connect
dbname = 'wbtaflae'
user = 'wbtaflae'
password = 'PrFRj3SJLlpPBhmG8I0SY3ogazL6bmGz'
host = 'salt.db.elephantsql.com'

rpg_conn = psycopg2.connect( dbname =dbname, user=user, password=password, host=host)

print(rpg_conn)

#create the cursor once we established a connection to database server
rpg_curs = rpg_conn.cursor()
#once the cursor is established, we can now execute quires command
rpg_curs.execute('SELECT * FROM test_table;')

#this is the code to look at content of table.
rpg_curs.fetchall()

import sqlite3

#open connection to sql3
rpg_conn = sqlite3.connect('C:\\Users\\D3MoNa\\PycharmProjects\\Month3\\SQLAndDataBase\\module1-introduction-to-sql\\rpg_db.sqlite3')

#similar after connect to database we need a cursor
rpg_curs = rpg_conn.cursor()

#count how many character there are
print(rpg_curs.execute('select count(*) From charactercreator_character').fetchall())

#count how many unique names there are
print(rpg_curs.execute('select COUNT(distinct name) FROM charactercreator_character').fetchall())

#
character = rpg_curs.execute('SELECT * from charactercreator_character;').fetchall()

print(character[0],
character[-1],
len(character))

#get table schema. information to use to query tables in posques.
print('\n' , rpg_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall())

#create the table for SQL.
create_character_tables = """
    CREATE TABLE charactercreator_characters(
    character_id Serial Primary key,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT 
    );
"""

#just to show that we have an empty tables
#rpg_curs.execute(create_character_tables)

#show_tables = """
#SELECT *
#FROM pg_catalog.pg_tables
#WHERE schemaname != 'pg_catalog'
#AND schemaname != 'information_schema';
#"""
#rpg_curs.execute(show_tables)


rpg_curs.fetchall()

##turn into a string
##[1:] chop off the index. "serialNumber"

example_insert = """INSERT INTO charactercreator_character (name, level, exp, hp, strength, intelligence, dexterity, wisdom) VALUES """ + str(character[0][1:])
print(example_insert)

#how to do this for all rows? 302...

for character in character:
  insert_character = """
    INSERT INTO charactercreator_characters
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ';'
  rpg_curs.execute(insert_character)

print(insert_character)

rpg_curs.execute('SELECT * FROM charactercreator_characters;')
print(rpg_curs.fetchall())

rpg_curs.close()
rpg_conn.commit()

rpg_curs=rpg_conn.cursor()
rpg_curs.execute('SELECT * FROM charactercreator_characters;')
rpg_characters = rpg_curs.fetchall()


#do a for loop to check chracter is the same as
#for character, pg_character in zip(characters, pg_characters):
#  assert character == pg_character
