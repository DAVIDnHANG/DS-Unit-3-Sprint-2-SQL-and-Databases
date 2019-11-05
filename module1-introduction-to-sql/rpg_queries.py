import sqlite3
import os.path

base_dir = os.path.dirname(os.path.abspath('module1-introduction-to-sql'))
db_path = os.path.join("base_dir",'rpg_db.sqlite3')
print(os.listdir())
#connect function, which return connection object
conn = sqlite3.connect('C:\\Users\\D3MoNa\\PycharmProjects\\Month3\\SQLAndDataBase\\module1-introduction-to-sql\\rpg_db.sqlite3')
#cursor allows us to execute SQL queries
cur=conn.cursor()
print(dir(cur))

#we can execute a query against the database with the aptly name execute method
cur.execute("select sum(character_id) from charactercreator_character ")
results = cur.fetchall()
print(results)
cur.execute("select sum(character_ptr_id) from charactercreator_cleric")
results = cur.fetchall()
print(results)
cur.execute('select sum(character_ptr_id) from charactercreator_mage')
results = cur.fetchall()
print(results)
cur.execute('select sum(character_ptr_id) from charactercreator_necromancer')
results = cur.fetchall()
print(results)
cur.execute()
cur.execute(select charactercreator_character_inventory.character_id
COUNT(*)
FROM charactercreator_character_inventory as t1, armory_item as t2, charactercreator_character as t3,
WHERE charactercreator_character_inventory.item_id = armory_item.item_id and charactercreator_character.character_id = charactercreator_character_inventory.character_id)
results = cur.fetchall()
print(results)
cur.execute()


#need to FETCH, then assign results to variable
results = cur.fetchall()
print(results)


cur.close()
conn.close()