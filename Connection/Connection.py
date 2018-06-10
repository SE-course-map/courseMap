import json
import MySQLdb

from Common.Exceptions import DbException


def getCourseMapConnectionString():
    try:
        jsonFile = open("SetUp/ConnectionStrings.json", "r")

        connectionString = json.loads(jsonFile.read())["courseMap"]

        jsonFile.close()

        return connectionString
    except:
        raise DbException("Cannot get connection string")


def cursorDecorator(func):
    def _decorate(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise DbException(str(e))

    _decorate.__name__ = func.__name__
    return _decorate


class Cursor:
    def __init__(self, cursor):
        self.cursor = cursor

    @cursorDecorator
    def execute(self, operation, params=None):
        self.cursor.execute(operation, params)

    @cursorDecorator
    def fetchone(self):
        return self.cursor.fetchone()

    @cursorDecorator
    def fetchall(self):
        return self.cursor.fetchall()

    @cursorDecorator
    def rowcount(self):
        return self.cursor.rowcount


class CourseMapConnection:

    connectionInfo = {}
    for item in getCourseMapConnectionString().split(';'):
        if item.strip() == "":
            continue
        name, value = item.split('=')
        connectionInfo[name] = value

    def __init__(self):
        self.db = None

    def __enter__(self):
        try:
            self.db = MySQLdb.connect(
                host=CourseMapConnection.connectionInfo["Server"],
                user=CourseMapConnection.connectionInfo["Uid"],
                passwd=CourseMapConnection.connectionInfo["Pwd"],
                db=CourseMapConnection.connectionInfo["Database"],
                charset='utf8'
            )
            self.db.autocommit(True)
            return self
        except:
            raise DbException("Cannot connect to course map database")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()
        self.db = None

    def cursor(self):
        if self.db is None:
            raise DbException("use `with` keyword")
        return Cursor(self.db.cursor())
