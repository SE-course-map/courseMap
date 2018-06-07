from Connection.Connection import *
from Essence.Year import *


class YearController:
    @staticmethod
    def add(year):
        year.validate()

        with CourseMapConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(""" INSERT INTO year (position) VALUES (%s) """, (year.position, ))

    @staticmethod
    def remove(yearId):
        with CourseMapConnection() as connection:
            cursor = connection.cursor()

            cursor.execute(""" DELETE FROM year WHERE id=%s """, (yearId, ))

    @staticmethod
    def getAllYearInfo():
        with CourseMapConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(""" SELECT id, position FROM year """)
            return cursor.fetchall()