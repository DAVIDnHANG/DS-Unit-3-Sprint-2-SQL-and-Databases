import psycopg2
import sqlite3

#setting up for psycopy2.connect
dbname = 'wbtaflae'
user = 'wbtaflae'
password = ''
host = 'salt.db.elephantsql.com'

rpg_conn = psycopg2.connect( dbname =dbname, user=user, password=password, host=host)

#create the cursor once we established a connection to database server
rpg_curs = rpg_conn.cursor()
#once the cursor is established, we can now execute quires command
rpg_curs.execute('SELECT * FROM test_table;')

import sqlite3

sl_conn = sqlite3.connect('C:\\Users\\D3MoNa\\PycharmProjects\\Month3\\SQLAndDataBase\\module1-introduction-to-sql\\rpg_db.sqlite3')
sl_curs = sl_conn.cursor()
items = sl_curs.execute('SELECT * from charactercreator_character_inventory').fetchall()

sl_curs.execute('PRAGMA table_info(charactercreator_character_inventory);').fetchall()

#create_character_table_two = """
#CREATE TABLE charactercreator_character_inventory_web (
#character_id SERIAL PRIMARY KEY,
#name VARCHAR(30),
#item_id INT
#);
#"""
#rpg_curs.execute(create_character_table_two)

for item in items:
  insert_item = """INSERT INTO charactercreator_character_inventory_web (name, item_id) VALUES""" + str(item[1:]) + ';'
  rpg_curs.execute(insert_item)

rpg_curs.execute('SELECT * from charactercreator_character_inventory_web')
print(rpg_curs.fetchall())


#make the table for titanic table
create_titanic_table = """ 
CREATE TABLE titanic (
Survived INT,
Pclass INT,
Name VARCHAR(30),
Sex VARCHAR(15),
Age INT,
SiblingsSpousesAboard INT,
ParentsChildrenAboard INT,
Fare FLOAT);
"""
#insert the row in dataframe into table
#create column list for insertion
df.head(0).to_sql('table_name', engine, if_exists='replace',index=False) #truncates the table

conn = engine.raw_connection()
cur = conn.cursor()
output = io.StringIO()
df.to_csv(output, sep='\t', header=False, index=False)
output.seek(0)
contents = output.getvalue()
cur.copy_from(output, 'table_name', null="") # null values become ''
conn.commit()








rpg_curs.close()
rpg_conn.commit()
