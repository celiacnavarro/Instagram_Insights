-- Write an SQL query to solve the given problem statement.
-- Find users who have ever commented on a photo

SELECT username,comment_text 
FROM users 
LEFT JOIN comments ON users.id = comments.user_id 
GROUP BY users.id 
HAVING comment_text IS NOT NULL;