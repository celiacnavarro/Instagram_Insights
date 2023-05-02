-- Write an SQL query to solve the given problem statement.
-- Our Investors want to know...How many times does the average user post? (total number of photos/total number of users)

SELECT ROUND((SELECT COUNT(*)FROM photos)/(SELECT COUNT(*) FROM users),2)
