-- Write an SQL query to solve the given problem statement.
-- user ranking by postings higher to lower

SELECT users.username, COUNT(photos.image_url)
FROM users
LEFT JOIN photos ON users.id = photos.user_id
GROUP BY users.id
ORDER BY COUNT(photos.image_url) DESC
LIMIT 74;