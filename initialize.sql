use pzb4me_media;
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(20),
    gender VARCHAR(6),
    age INT
)
use pzb4me_media;
CREATE TABLE posts (
    post_id INT PRIMARY KEY,
    user_id INT FOREIGN KEY,
    date/time DATETIME,
    likes INT
)

INSERT INTO users (user_id, username, gender, age) VALUES (1, "Abby Anderson", "Female", 22);
INSERT INTO users (user_id, username, gender, age) VALUES (2, "Brian Brown", "Male", 19);
INSERT INTO users (user_id, username, gender, age) VALUES (3, "Carlin Charleston", "Female", 31);
INSERT INTO users (user_id, username, gender, age) VALUES (4, "Daniel Davis", "Male", 25);
INSERT INTO posts (post_id, user_id, date/time, likes) VALUES (1, 1, "2024-09-30 10:00:00", 51);
INSERT INTO posts (post_id, user_id, date/time, likes) VALUES (2, 2, "2025-02-20 12:10:00", 121);
INSERT INTO posts (post_id, user_id, date/time, likes) VALUES (3, 1, "2025-05-13 10:30:00", 110);
INSERT INTO posts (post_id, user_id, date/time, likes) VALUES (4, 3, "2025-09-02 19:30:00", 28);
INSERT INTO posts (post_id, user_id, date/time, likes) VALUES (5, 4, "2025-12-25 24:00:00", 300);
INSERT INTO posts (post_id, user_id, date/time, likes) VALUES (6, 3, "2026-01-01 00:00:00", 235);

