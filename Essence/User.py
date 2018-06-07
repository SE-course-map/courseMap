from flask import request

from Common.Exceptions import *


kMinPasswordLength = 4
kMinUserNameLength = 4


class User:
    @staticmethod
    def getFromForm():
        try:
            return User(request.form["userName"], request.form["rawPassword"])
        except Exception as e:
            raise FormException(str(e))

    def __init__(self, userName, rawPassword):
        self.userName = userName
        self.rawPassword = rawPassword

    def validate(self):
        if len(self.userName) < kMinUserNameLength:
            raise EmptyUserNameException("User Name is too short")
        if len(self.rawPassword) < kMinPasswordLength:
            raise PasswordLengthException("Password is too short")