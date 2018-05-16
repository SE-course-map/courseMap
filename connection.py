import MySQLdb


class AbstractConnection:
    def __init__(
        self,
        host,
        user,
        passwd,
        db
    ):
        self.db = MySQLdb.connect(
            host=host,
            user=user,
            passwd=passwd,
            db=db
        )
        self.db.autocommit(True)

    def getCursor(self):
        return self.db.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()


class CourseMapConnection(AbstractConnection):
    def __init__(self):
        super().__init__(
            'localhost',
            'courseMapUser',
            '1111',
            'courseMap'
        )