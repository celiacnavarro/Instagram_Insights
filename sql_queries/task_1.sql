-- Write an SQL query to solve the given problem statement.
-- What day of the week do most users register on? 
-- We need to figure out when to schedule an ad campgain

SELECT id, username, created_at
FROM users 
ORDER BY created_at 
ASC LIMIT 5
