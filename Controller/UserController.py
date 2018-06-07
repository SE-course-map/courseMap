from Connection.Connection import *
from Common.Login import *
from Essence.User import *


class UserController:
    @staticmethod
    def add(user):
        user.validate()

        salt = generateSalt()
        password = hashPassword(user.rawPassword, salt)

        with CourseMapConnection() as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO users (userName, password, salt) VALUES (%s, %s, %s)""",
                           (user.userName, password, salt))

    @staticmethod
    def check(user):
        with CourseMapConnection() as connection:
            cursor = connection.cursor()
            cursor.execute("""SELECT password, salt FROM users WHERE userName=%s""", (user.userName,))
            if cursor.rowcount() == 0:
                return False

            row = cursor.fetchone()

            expectedPassword = row[0]
            salt = row[1]

            return hashPassword(user.rawPassword, salt) == expectedPassword

    @staticmethod
    def remove(userId):
        with CourseMapConnection() as connection:
            cursor = connection.cursor()
            cursor.execute("""DELETE FROM users WHERE id=%s""", (userId,))

    @staticmethod
    def getAllUsersInfo():
        with CourseMapConnection() as connection:
            cursor = connection.cursor()
            cursor.execute("""SELECT id, userName FROM users""")
            return cursor.fetchall()