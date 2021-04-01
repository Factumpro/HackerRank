SELECT 
    city,
    LENGTH(city)
FROM 
    station
WHERE 
    LENGTH(city) 
    IN (
        SELECT 
            MAX(LENGTH(city))
        FROM 
            station
        UNION          
        SELECT 
            MIN(LENGTH(city))
        FROM 
            station
        )
ORDER BY 
    LENGTH(city) DESC,
    city ASC LIMIT 2;
