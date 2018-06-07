-- set up year table
CREATE TABLE courseMap.year(
    id INT NOT NULL AUTO_INCREMENT,
    position TINYINT NOT NULL,
    PRIMARY KEY(id),
    UNIQUE (position)
) ENGINE = INNODB;