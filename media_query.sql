SELECT * FROM users WHERE age > 23;

SELECT users.user_id, posts.user_id
FROM users
LEFT JOIN posts on users.user_id = posts.user_id;

