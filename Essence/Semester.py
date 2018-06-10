from flask import request

from Common.Exceptions import *
from Essence.AbstractEssence import *


kMinSemesterPositionNum = 1
kMaxSemesterPositionNum = 10


class Semester(AbstractEssence):
    @staticmethod
    def getFromForm():
        try:
            return Semester(request.form['name'], request.form['yearId'], request.form['position'])
        except Exception as e:
            raise FormException(str(e))

    def __init__(self, name, yearId, position):
        super().__init__()
        self.name = name
        self.yearId = int(yearId)
        self.position = int(position)

    def validate(self):
        if self.position < kMinSemesterPositionNum or self.position > kMaxSemesterPositionNum:
            raise SemesterPositionException("Invalid position value")
        if self.name == "":
            raise SemesterEmptyNameException("Semester Name cannot be empty")
