-- Write an SQL query to solve the given problem statement.
-- We want to target our inactive users with an email campaign. Find the users who have never posted a photo.

SELECT username
FROM users
LEFT JOIN 
    photos 
ON 
    users.id = photos.user_id 
WHERE 
    photos.id IS NULL;
