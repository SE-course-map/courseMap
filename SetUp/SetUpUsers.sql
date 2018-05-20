-- set up users table
CREATE TABLE courseMap.users(
    id INT NOT NULL AUTO_INCREMENT,
    userName CHAR(32) NOT NULL,
    password CHAR(32) NOT NULL,
    salt CHAR(32) NOT NULL,
    PRIMARY KEY(id),
    UNIQUE (userName)
);