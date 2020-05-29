import sqlite3 
import os

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg.db")
conn = sqlite3.connect('rpg.db')
curs = conn.cursor()

# How many tottal Characters are there? 302
query_1 = 'SELECT COUNT(name)FROM charactercreator_character;'

# How many from each specific subclass? (75, 68, 108, 51, 11)
query_cleric = 'SELECT Count(character_ptr_id)FROM charactercreator_cleric;' 
query_fighter = 'SELECT Count(character_ptr_id)FROM charactercreator_fighter;'
query_mage = 'SELECT Count(character_ptr_id)FROM charactercreator_mage;'
query_thief = 'SELECT Count(character_ptr_id)FROM charactercreator_thief;'
query_necromancer = 'SELECT Count(mage_ptr_id)FROM charactercreator_necromancer;'

# How many total items? 
query_total_items = 'SELECT count(item_id)FROM armory_item;'

# How many of the items are weapons? How many are not? (37)
query_weapons = 'SELECT count(ai.item_id),ai.NAME FROM armory_item AS ai INNER JOIN armory_weapon AS AW ON item_id=item_ptr_id;'

# How many items does each character have? (Return first 20 rows) 

query_items_char = 'SELECT cci.character_id,count(cci.item_id)AS itemcount,ai.name FROM armory_item AS ai LEFT JOIN charactercreator_character_inventory AS cci ON cci.item_id=ai.item_id GROUP BY ai.name ORDER BY itemcount DESC LIMIT 20;'

# How many weapons does each character have? (Return first 20 rows)
query_weapons_char = 'SELECT cci.character_id,ai.item_id,count(aw.item_ptr_id)AS weapon_count FROM charactercreator_character_inventory;'

# On average, how many items does each Character have? 
query_avg_items = 'SELECT AVG(itemcount)FROM(SELECT cci.character_id,count(DISTINCT cci.item_id)AS itemcount,ai.name FROM charactercreator_character_inventory AS cci LEFT JOIN armory_item AS ai ON cci.item_id=ai.item_id GROUP BY cci.character_id);'

# On average, how many weapons does each character have? 
query_ave_weapons = 'SELECT AVG(weapon_count)FROM(SELECT cci.character_id,ai.item_id,count(aw.item_ptr_id)AS weapon_count FROM charactercreator_character_inventory AS cci LEFT JOIN armory_item AS ai ON cci.item_id=ai.item_id LEFT JOIN armory_weapon AS aw ON aw.item_ptr_id=ai.item_id ORDER BY weapon_count DESC);'