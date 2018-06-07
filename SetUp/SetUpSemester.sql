-- set up semester table
CREATE TABLE courseMap.semester(
    id INT NOT NULL AUTO_INCREMENT,
    name CHAR(32) NOT NULL,
    yearId INT NOT NULL,
    position TINYINT NOT NULL,

    FOREIGN KEY(yearId)
        REFERENCES courseMap.year(id)
        ON DELETE RESTRICT
        ON UPDATE RESTRICT,

    PRIMARY KEY(id),
    UNIQUE(name)
) ENGINE = INNODB;