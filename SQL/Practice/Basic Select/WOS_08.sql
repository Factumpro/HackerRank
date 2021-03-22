SELECT 
    DISTINCT city 
FROM 
    station 
WHERE 
    city 
        REGEXP '^[aeiou]' 
    AND 

    city 
        REGEXP '[aeiou]$'