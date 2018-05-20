from flask import request

class User:
    @staticmethod
    def getFromForm():
        return User(request.form['userName'], request.form['rawPassword'])

    def __init__(self, userName, rawPassword):
        self.userName = userName
        self.rawPassword = rawPassword