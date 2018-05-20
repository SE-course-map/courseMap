import json
import MySQLdb

def getCourseMapConnectionString():
    jsonFile = open("SetUp/ConnectionStrings.json", "r")

    connectionString = json.loads(jsonFile.read())["courseMap"]

    jsonFile.close()

    return connectionString


class CourseMapConnectionError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


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
        self.db = MySQLdb.connect(
            host=CourseMapConnection.connectionInfo["Server"],
            user=CourseMapConnection.connectionInfo["Uid"],
            passwd=CourseMapConnection.connectionInfo["Pwd"],
            db=CourseMapConnection.connectionInfo["Database"]
        )
        self.db.autocommit(True)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()
        self.db = None

    def cursor(self):
        if self.db is None:
            raise CourseMapConnectionError("use `with` keyword")
        return self.db.cursor()
