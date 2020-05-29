-- How many total Characters are there? 302
 -- SELECT COUNT(name)FROM charactercreator_character
 -- How many of each specific subclass?
 -- cleric - 75
 -- fighter - 68
 -- mage -- 108
 -- necromancer - 11
 -- theif -- 51
 --SELECT count(character_ptr_id)FROM charactercreator_thief
 --How many total items? 174 
 -- select count(item_id)from armory_item
 
 --How many of the items are weapons? How many are not? 
 
 --SELECT count(ai.item_id),  
 --	ai.NAME
 --From armory_item as ai
 --INNER JOIN armory_weapon as AW
 --ON item_id = item_ptr_id
 ------------------------------
 
 --How many Items does each character have? (Return first 20 rows)
/* 
SELECT cci.character_id, count(cci.item_id) as itemcount, ai.name
FROM armory_item as ai
LEFT JOIN  charactercreator_character_inventory as cci
ON cci.item_id = ai.item_id
GROUP BY ai.name
ORDER BY itemcount DESC  
LIMIT 20 
*/

-- Five 
/*
SELECT cci.character_id, count(DISTINCT cci.item_id) as itemcount, ai.name
FROM charactercreator_character_inventory as cci
LEFT JOIN  armory_item as ai
ON cci.item_id = ai.item_id
GROUP BY cci.character_id
ORDER BY itemcount DESC  
LIMIT 20 
*/

/*
SELECT
        ccc.character_id,
        ccc.name,
        count(cci.item_id) as item_count_per_char
    FROM
        charactercreator_character as ccc
    LEFT JOIN charactercreator_character_inventory as cci 
        on ccc.character_id = cci.character_id
    LEFT JOIN armory_item as ai 
        on cci.item_id = ai.item_id
    GROUP by
        ccc.name
    ORDER BY
        item_count_per_char DESC
*/
-- How many Weapons does each character have? (Return first 20 rows)
/*
SELECT cci.character_id, ai.item_id, count(aw.item_ptr_id) as weapon_count
FROM  charactercreator_character_inventory as cci
LEFT JOIN  armory_item as ai
ON cci.item_id = ai.item_id
LEFT JOIN armory_weapon as aw
ON aw.item_ptr_id = ai.item_id
GROUP BY cci.character_id
ORDER by weapon_count DESC


-- On average, how many Weapons does each character have?

/*SELECT AVG(weapon_count)
FROM

(SELECT cci.character_id, ai.item_id, count(aw.item_ptr_id) as weapon_count
FROM  charactercreator_character_inventory as cci
LEFT JOIN  armory_item as ai
ON cci.item_id = ai.item_id
LEFT JOIN armory_weapon as aw
ON aw.item_ptr_id = ai.item_id
GROUP BY cci.character_id
ORDER by weapon_count DESC)
*/

-- On average, how many Items does each Character have?
SELECT AVG(itemcount)
FROM

(SELECT cci.character_id, count(DISTINCT cci.item_id) as itemcount, ai.name
FROM charactercreator_character_inventory as cci
LEFT JOIN  armory_item as ai
ON cci.item_id = ai.item_id
GROUP BY cci.character_id)