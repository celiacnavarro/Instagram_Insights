-- Write an SQL query to solve the given problem statement.
-- We also have a problem with celebrities. Find users who have never commented on a photo

SELECT username, comments.comment_text
FROM users
LEFT JOIN comments
ON users.id = comments.user_id
WHERE comments.comment_text IS NULL;
