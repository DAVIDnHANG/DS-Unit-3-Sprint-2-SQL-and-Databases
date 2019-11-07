#!curl ipecho.net/plain
#107.196.176.232  <the whitelist IP address i am using
#username: Dhang
#password : 6IVZdpb4fuu4390y
import pymongo

client = pymongo.MongoClient("mongodb://Dhang:6IVZdpb4fuu4390y@cluster0-shard-00-00-l6ply.azure.mongodb.net:27017,cluster0-shard-00-01-l6ply.azure.mongodb.net:27017,cluster0-shard-00-02-l6ply.azure.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test


#db is how many computer are working


#check how many machine are working
print(client.nodes)
print(db)

import sqlite3
import os.path

base_dir = os.path.dirname(os.path.abspath('module1-introduction-to-sql'))
db_path = os.path.join("base_dir",'rpg_db.sqlite3')
print(os.listdir())
sl_conn = sqlite3.connect('C:\\Users\\D3MoNa\\PycharmProjects\\Month3\\SQLAndDataBase\\module1-introduction-to-sql\\rpg_db.sqlite3')
sl_curs = sl_conn.cursor()
items = sl_curs.execute('SELECT * from charactercreator_character_inventory').fetchall()

sl_curs.execute('PRAGMA table_info(charactercreator_character_inventory);').fetchall()
#make a character_character_inventory

charactercreator_character_inventory = (1,2,3)
db.test.insert_one({'charactercreator_character_inventory' : charactercreator_character_inventory})
db.test.insert_one({
    'id': charactercreator_character_inventory[0],
    'name':charactercreator_character_inventory[1],
    'hp':charactercreator_character_inventory[2]
})

for item in items:
    id = item[0]
    character_id = item[1]
    item_id=item[2]
    print(id,character_id,item_id)
    db.test.insert_one({
    'id': item[0],
    'name':item[1],
    'hp':item[2]
    })



print(list(db.test.find({'charactercreator_character_inventory':item_id})))