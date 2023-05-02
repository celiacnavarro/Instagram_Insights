-- Write an SQL query to solve the given problem statement.

-- Find the 5 oldest users.

SELECT id, username, created_at
FROM users 
ORDER BY created_at 
ASC LIMIT 5
