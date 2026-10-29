SELECT users.username, users.age, posts.post_id, posts.datetime, posts.likes
FROM users
JOIN posts ON users.user_id = posts.user_id
WHERE users.age > 23;
