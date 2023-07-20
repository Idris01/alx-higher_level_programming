-- Print score and name where name is present
SELECT score, name FROM second_table WHERE name is not NULL and TRIM(name) != '' ORDER BY score DESC;
