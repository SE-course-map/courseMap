from connection import CourseMapConnection as Connection

def addUser(name, password, salt):
    with Connection() as connection:
        cursor = connection.getCursor()
        cursor.execute(
            """INSERT INTO courseMap.users (userName, password, salt) VALUES (%s, %s, %s)""",
            (name, password, salt)
        )