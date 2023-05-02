-- Write an SQL query to solve the given problem statement.
-- What day of the week do most users register on? 
-- We need to figure out when to schedule an ad campgain

SELECT 
    DAYNAME(created_at) AS day_of_week, 
    COUNT(*) AS count
FROM 
    users 
GROUP BY 
    day_of_week 
ORDER BY 
    count DESC 
LIMIT 
    1;
