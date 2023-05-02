--  Write an SQL query to solve the given problem statement.
--  Write an SQL query to solve the given problem statement.

SELECT username, comments.comment_text
FROM users
LEFT JOIN comments
ON users.id = comments.user_id
WHERE comments.comment_text IS NULL;
