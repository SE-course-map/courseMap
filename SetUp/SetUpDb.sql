-- set up database and create corresponding user
CREATE DATABASE courseMap;
GRANT ALL PRIVILEGES ON courseMap.* TO 'courseMapUser'@'localhost' IDENTIFIED BY '1111';
