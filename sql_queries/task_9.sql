-- Write an SQL query to solve the given problem statement.
-- A brand wants to know which hashtags to use in a post. What are the top 5 most commonly used hashtags?

SELECT tags.tag_name, COUNT(*) AS count
FROM photo_tags
JOIN tags 
ON photo_tags.tag_id = tags.id 
GROUP BY photo_tags.tag_id
ORDER BY count DESC

