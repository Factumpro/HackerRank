SELECT
    DISTINCT city 
FROM 
    station 
WHERE
    city 
        REGEXP '^[^aeiou]' 
    OR 
    city 
        REGEXP '[^aeiou]$'
