from flask import session


class SessionController:
    @staticmethod
    def check():
        return 'username' in session

    @staticmethod
    def set(user):
        session['username'] = user.userName

    @staticmethod
    def remove():
        session.clear()