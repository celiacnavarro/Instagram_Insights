-- Write an SQL query to solve the given problem statement.
-- Total Posts by users (longer versionof SELECT COUNT(*)FROM photos)

SELECT SUM(post_count) AS total_posts
FROM (
  SELECT COUNT(*) AS post_count
  FROM photos
  GROUP BY user_id
) subquery;