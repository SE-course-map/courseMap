from Essence.Semester import *
from Connection.Connection import *


class SemesterController:
    @staticmethod
    def add(semester):
        semester.validate()

        if SemesterController.check(semester.yearId, semester.position):
            raise SemesterPositionException("Semester with given year and position already exist")

        with CourseMapConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                """ INSERT INTO semester (name, yearId, position) VALUES (%s, %s, %s) """,
                (semester.name, semester.yearId, semester.position)
            )

    @staticmethod
    def check(yearId, position):
        with CourseMapConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                """ SELECT (id) FROM semester WHERE yearId=%s AND position=%s """,
                (yearId, position)
            )
            return cursor.rowcount() > 0

    @staticmethod
    def update(semesterId, newSemester):
        newSemester.validate()

        with CourseMapConnection() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """ SELECT (id) FROM semester WHERE yearId=%s AND position=%s """,
                (newSemester.yearId, newSemester.position)
            )

            if cursor.rowcount() > 0 and cursor.fetchone()[0] != semesterId:
                raise SemesterPositionException("Semester with given year and position already exist")

            cursor.execute(
                """ UPDATE semester SET name=%s, yearId=%s, position=%s WHERE id=%s """,
                (newSemester.name, newSemester.yearId, newSemester.position, semesterId)
            )

    @staticmethod
    def remove(semesterId):
        with CourseMapConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(""" DELETE FROM semester WHERE id=%s """, (semesterId, ))

    @staticmethod
    def getAllSemesterInfo():
        with CourseMapConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(""" SELECT id, name, yearId, position FROM semester """)
            return cursor.fetchall()
