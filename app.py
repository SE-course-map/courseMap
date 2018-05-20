import os
import sys


projectRootDirectory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
sys.path.append(projectRootDirectory)


from flask import Flask, render_template, request, redirect, url_for, flash
from UserController.UserController import UserController, UserControllerError
from UserController.User import User
from SessionController.SessionController import SessionController
from Common.Common import getRandomString


app = Flask(__name__)
app.secret_key = getRandomString(10)


def protected(func):
    def _decorate(*args, **kwargs):
        if not SessionController.check():
            flash('Session has expired', 'error')
            return redirect(url_for('adminLogin'))
        return func(*args, **kwargs)

    _decorate.__name__ = func.__name__
    return _decorate


@app.route('/admin/', methods=['GET'])
@protected
def admin():
    return render_template('admin.html')


@app.route('/admin/login/', methods=['GET', 'POST'])
def adminLogin():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        user = User.getFromForm()
        if UserController.check(user):
            SessionController.set(user)
            flash('Hello, %s' % (user.userName, ), 'info')
            return redirect(url_for('admin'))
        else:
            flash('No such a user or password is incorrect', 'error')
            return redirect(url_for('adminLogin'))


@app.route('/admin/register', methods=['POST', 'GET'])
@protected
def adminRegister():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        user = User.getFromForm()

        try:
            UserController.add(user)
            flash('user %s was added successfully' % (user.userName, ), 'info')
            return redirect(url_for('admin'))
        except UserControllerError as e:
            flash('Cannot create user: %s' % (str(e), ), 'error')
        except Exception as e:
            flash('Cannot create user: username already exists or database error', 'error')

        return redirect(url_for('adminRegister'))


@app.route('/admin/logout/', methods=['GET'])
def adminLogout():
    SessionController.remove()
    flash('You were logged out', 'info')
    return redirect(url_for('adminLogin'))


@app.route('/admin/users', methods=['GET'])
@protected
def adminUsers():
    try:
        users = UserController.getAllUsersInfo()
        return render_template('users.html', users=users)
    except Exception as e:
        flash('Database error', 'error')
        return redirect(url_for('admin'))


@app.route('/admin/users/<int:id>', methods=['DELETE'])
@protected
def deleteUser(id):
    try:
        UserController.remove(id)
        flash('Success', 'info')
    except Exception as e:
        flash('Database error', 'error')
    finally:
        return redirect(url_for('admin'))


if __name__ == '__main__':
    app.run(debug=True)