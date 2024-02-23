-- selects score with names from table seccond table.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER by score DESC;
