-- Write an SQL query to solve the given problem statement.
-- We have a small problem with bots on our site. Find users who have liked every single photo on the site

SELECT users.id, users.username, COUNT(DISTINCT photo_id) AS total_likes_by_user
FROM users
JOIN likes
ON users.id = likes.user_id
GROUP BY likes.user_id
HAVING COUNT(DISTINCT photo_id) = (SELECT COUNT(*) FROM photos);
