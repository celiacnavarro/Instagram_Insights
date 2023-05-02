-- Write an SQL query to solve the given problem statement
-- Total numbers of users who have posted at least one time

SELECT COUNT(DISTINCT user_id) AS total_number_of_users_with_posts
FROM photos

