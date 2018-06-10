-- set up course table
CREATE TABLE courseMap.course(
    id INT NOT NULL AUTO_INCREMENT,
    name CHAR(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    forCS BOOL NOT NULL,
    forBA BOOL NOT NULL,
    semesterId INT NOT NULL,
    blockId INT NOT NULL,
    description TEXT CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    prerequisites TEXT CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    outcomes TEXT CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    credits FLOAT(3, 1),
    teacher CHAR(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    isEnglish BOOL NOT NULL,

    PRIMARY KEY(id),
    UNIQUE(name),

    FOREIGN KEY(semesterId)
        REFERENCES courseMap.semester(id)
        ON DELETE RESTRICT
        ON UPDATE RESTRICT,

    FOREIGN KEY(blockId)
        REFERENCES courseMap.block(id)
        ON UPDATE RESTRICT
        ON DELETE RESTRICT

) ENGINE = INNODB;