-- Write an SQL query to solve the given problem statement.
-- We're running a new contest to see who can get the most likes on a single photo. WHO WON?

SELECT users.username, photos.id, photos.image_url, COUNT(*) AS Total_Likes
FROM 
    photos 
JOIN 
    users 
ON 
    photos.user_id = users.id 
LEFT JOIN 
    likes 
ON 
    photos.id = likes.photo_id 
GROUP BY 
    photos.id 
ORDER BY 
    COUNT(*) DESC 
LIMIT 
    1;