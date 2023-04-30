# Instagram_Insights
Analysing User Behaviour on Instagram using Python and SQL

## Description
The HiCounselor Instagram Insights project aims to provide data-driven insights for businesses looking to improve their social media strategy. By cleaning and analyzing Instagram data using SQL queries, the project allows businesses to gain valuable information about user behavior, engagement, and posting patterns. The insights generated can be used to make informed decisions and optimize social media campaigns for maximum impact.

## Requirements
pandas==1.3.4

numpy==1.21.4

## Directory tree

```
Instagram_insights
│   README.md
│   requirements.txt
│   db.py
│
└───data
│   │   comments.csv
|   |   follows.csv
|   |   ...
│   └─── cleaned_data
│   │   │   comments_cleaned.csv
│   │   │   follows_cleaned.csv
│   │   │   ...
│
└───data_cleaning
│   │   comments.py
│   │   follows.py
│   │   ...
|
└───sql_queries
│   │   task_1.sql
│   │   task_10.sql
│   │   ...

 ```
 ## Database Diagram
 
 ![Database Diagram](https://github.com/celiacnavarro/Instagram_Insights/blob/main/database_diagram.png "Database Diagram")
 
 ## Examples of SQL Queries for Analyzing Instagram Data
 
The following SQL queries are just a small selection of the analyses that can be performed with the Instagram data provided by HiCounselor. These queries illustrate some of the insights that can be gained by cleaning and analyzing the data, and can serve as examples for further analysis.

**- Contest Winner:** This query finds the user who has received the most likes on a single photo. It can be used to determine the winner of a contest based on Instagram likes.
```
SELECT users.username, photos.id, photos.image_url, COUNT(*) AS Total_Likes
FROM photos 
JOIN users 
ON photos.user_id = users.id 
LEFT JOIN likes 
ON photos.id = likes.photo_id 
GROUP BY photos.id 
ORDER BY COUNT(*) DESC 
LIMIT 1;
```

**- Top Hashtags:** This query finds the top 5 most commonly used hashtags in the dataset. It can be used to determine which hashtags are most popular and should be included in a post.
```
SELECT tags.tag_name, COUNT(*) AS count
FROM photo_tags
JOIN tags 
ON photo_tags.tag_id = tags.id 
GROUP BY photo_tags.tag_id
ORDER BY count DESC;
```

**- Bot and Celebrity Accounts:** This query calculates the percentage of users who have either never commented on a photo or have commented on every photo. It can be used to determine if a high percentage of the user base is made up of bots or celebrities.
```
SELECT tableA.total_A AS 'Number Of Users who never commented',
(tableA.total_A/(SELECT COUNT(*) FROM users))*100 AS '%',
tableB.total_B AS 'Number of Users who likes on every photos',
(tableB.total_B/(SELECT COUNT(*) FROM users))*100 AS '%'FROM(SELECT COUNT(*) AS total_A 
FROM(SELECT username,comment_text 
FROM users 
LEFT JOIN comments 
ON users.id =comments.user_id 
GROUP BY users.id 
HAVING comment_text IS NULL) 
AS total_number_of_users_without_comments) 
AS tableA 
JOIN(SELECT COUNT(*) AS total_B 
FROM(SELECT user_id AS id,username,count(*) AS total_likes_by_user 
FROM likes 
INNER JOIN users 
ON likes.user_id=users.id 
GROUP BY user_id 
HAVING COUNT(*) = (SELECT COUNT(*) FROM photos)) 
AS total_number_users_with_likes)
AS tableB;
```
