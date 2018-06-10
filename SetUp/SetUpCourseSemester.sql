CREATE TABLE courseMap.courseSemester(
    id INT NOT NULL AUTO_INCREMENT,
    courseId INT NOT NULL,
    semesterId INT NOT NULL,

    PRIMARY KEY(id),

    FOREIGN KEY(courseId)
        REFERENCES courseMap.course(id)
        ON DELETE RESTRICT
        ON UPDATE RESTRICT,

    FOREIGN KEY(semesterId)
        REFERENCES courseMap.semester(id)
        ON DELETE RESTRICT
        ON UPDATE RESTRICT

) ENGINE = INNODB;