-- set up block table
CREATE TABLE courseMap.block(
    id INT NOT NULL AUTO_INCREMENT,
    name CHAR(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    color CHAR(7) NOT NULL,
    PRIMARY KEY(id),
    UNIQUE(name)
) ENGINE = INNODB;