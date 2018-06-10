from flask import request

from Common.Exceptions import *
from Essence.AbstractEssence import *


kMinYearPositionNum = 1
kMaxYearPositionNum = 4


class Year(AbstractEssence):
    @staticmethod
    def getFromForm():
        try:
            return Year(int(request.form['position']))
        except Exception as e:
            raise FormException(str(e))

    def __init__(self, position):
        super().__init__()
        self.position = position

    def validate(self):
        if self.position < kMinYearPositionNum or self.position > kMaxYearPositionNum:
            raise YearPositionException("Invalid position value")
