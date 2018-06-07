import os
import sys


projectRootDirectory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
sys.path.append(projectRootDirectory)
APP_FILES = os.path.join(projectRootDirectory, 'static/database')

from flask import Flask, render_template, redirect, url_for, flash, get_flashed_messages, Response, jsonify

from Controller.UserController import *
from Controller.BlockController import *
from Controller.SessionController import *
from Controller.YearController import *
from Controller.SemesterController import *
from Controller.CourseController import *

from Essence.User import *
from Essence.Block import *
from Essence.Year import *

from Common.Common import *


app = Flask(__name__)
app.secret_key = getRandomString(10)


def protected(func):
    def _decorate(*args, **kwargs):
        if not SessionController.check():
            flash('Session has expired', 'error')
            return redirect(url_for('adminLogin')), 401
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
        try:
            user = User.getFromForm()
            if UserController.check(user):
                SessionController.set(user)
                get_flashed_messages()
                flash('Hello, %s' % (user.userName, ), 'info')
                return redirect(url_for('admin'))
            else:
                flash('No such a user or password is incorrect', 'error')
                return redirect(url_for('adminLogin'))
        except Exception as e:
            flash(str(e), 'error')
            return redirect(url_for('adminLogin'))


@app.route('/admin/register/', methods=['POST', 'GET'])
@protected
def adminRegister():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        try:
            user = User.getFromForm()
            UserController.add(user)
            flash('user %s was added successfully' % (user.userName, ), 'info')
            return redirect(url_for('admin'))
        except Exception as e:
            flash(str(e), 'error')
            return redirect(url_for('adminRegister'))


@app.route('/admin/logout/', methods=['GET'])
def adminLogout():
    SessionController.remove()
    flash('You were logged out', 'info')
    return redirect(url_for('adminLogin'))


@app.route('/admin/users/', methods=['GET'])
@protected
def adminUsers():
    try:
        users = UserController.getAllUsersInfo()
        return render_template('users.html', users=users)
    except Exception as e:
        flash(str(e), 'error')
        return redirect(url_for('admin'))


@app.route('/admin/users/<int:id>', methods=['DELETE'])
@protected
def deleteUser(id):
    try:
        UserController.remove(id)
        flash('Success', 'info')
        return Response(status=201)
    except Exception as e:
        flash(str(e), 'error')
        return Response(status=500)


@app.route('/admin/addBlock/', methods=['GET', 'POST'])
@protected
def addBlock():
    if request.method == 'GET':
        return render_template('addBlock.html')
    else:
        try:
            BlockController.add(Block.getFromForm())
            flash('success', 'info')
        except Exception as e:
            flash(str(e), 'error')
        return redirect(url_for('addBlock'))


@app.route('/admin/manageBlock/', methods=['GET', 'POST'])
@protected
def manageBlock():
    if request.method == 'GET':
        try:
            return render_template('manageBlock.html', blocks=BlockController.getAllBlockInfo())
        except Exception as e:
            flash(str(e), 'error')
            return redirect(url_for('admin'))
    else:
        try:
            block = Block.getFromForm()
            id = int(request.form['id'])

            BlockController.update(id, block)

            flash('success', 'info')
        except Exception as e:
            flash(str(e), 'error')
        return redirect(url_for('manageBlock'))


@app.route('/admin/manageBlock/<int:id>', methods=['DELETE'])
@protected
def deleteBlock(id):
    print('HELLO')
    try:
        BlockController.remove(id)
        flash('Success', 'info')
        return Response(status=201)
    except Exception as e:
        flash(str(e), 'error')
        return Response(status=500)


@app.route('/admin/addYear/', methods=['GET', 'POST'])
@protected
def addYear():
    if request.method == 'GET':
        return render_template(
            'addYear.html',
            minYear=kMinYearPositionNum,
            maxYear=kMaxYearPositionNum
        )
    else:
        try:
            YearController.add(Year.getFromForm())
            flash('success', 'info')
        except Exception as e:
            flash(str(e), 'error')
        return redirect(url_for('addYear'))


@app.route('/admin/manageYear/', methods=['GET'])
@protected
def manageYear():
    return render_template('manageYear.html', years=YearController.getAllYearInfo())


@app.route('/admin/manageYear/<int:id>', methods=['DELETE'])
@protected
def deleteYear(id):
    try:
        YearController.remove(id)
        flash('success', 'info')
        return Response(status=201)
    except Exception as e:
        flash(str(e), 'error')
        return Response(status=500)


@app.route('/admin/addSemester/', methods=['GET', 'POST'])
@protected
def addSemester():
    if request.method == 'GET':
        return render_template(
            'addSemester.html',
            years=YearController.getAllYearInfo(),
            minSemester=kMinSemesterPositionNum,
            maxSemester=kMaxSemesterPositionNum
        )
    else:
        try:
            SemesterController.add(Semester.getFromForm())
            flash('success', 'info')
        except Exception as e:
            flash(str(e), 'error')
        return redirect(url_for('addSemester'))


@app.route('/admin/manageSemester/', methods=['GET', 'POST'])
@protected
def manageSemester():
    if request.method == 'GET':
        return render_template(
            'manageSemester.html',
            years=YearController.getAllYearInfo(),
            semesters=SemesterController.getAllSemesterInfo(),
            minSemester=kMinSemesterPositionNum,
            maxSemester=kMaxSemesterPositionNum
        )
    else:
        try:
            id = int(request.form['id'])
            SemesterController.update(id, Semester.getFromForm())
            flash('success', 'info')
        except Exception as e:
            flash(str(e), 'error')
        return redirect(url_for('manageSemester'))


@app.route('/admin/manageSemester/<int:id>', methods=['DELETE'])
@protected
def deleteSemester(id):
    try:
        SemesterController.remove(id)
        flash('success', 'info')
        return Response(status=201)
    except Exception as e:
        flash(str(e), 'error')
        return Response(status=500)


@app.route('/admin/addCourse/', methods=['GET', 'POST'])
@protected
def addCourse():
    if request.method == 'GET':
        return render_template(
            'addCourse.html',
            semesters=SemesterController.getAllSemesterInfo(),
            blocks=BlockController.getAllBlockInfo()
        )
    else:
        try:
            CourseController.add(Course.getFromForm())
            flash('success', 'info')
        except Exception as e:
            flash(str(e), 'error')
        return redirect(url_for('addCourse'))



@app.route('/admin/manageCourse/', methods=['GET', 'POST'])
@protected
def manageCourse():
    if request.method == 'GET':
        return render_template(
            'manageCourse.html',
            semesters=SemesterController.getAllSemesterInfo(),
            blocks=BlockController.getAllBlockInfo(),
            courses=CourseController.getAllCourseInfo()
        )
    else:
        try:
            newCourse = Course.getFromForm()
            id = request.form['id']
            CourseController.update(id, newCourse)
            flash('success', 'info')
        except Exception as e:
            flash(str(e), 'error')
        return redirect(url_for('manageCourse'))


@app.route('/admin/manageCourse/<int:id>', methods=['DELETE'])
@protected
def deleteCourse(id):
    try:
        CourseController.remove(id)
        flash('success', 'info')
        return Response(status=201)
    except Exception as e:
        flash(str(e), 'error')
        return Response(status=500)


@app.route('/test/', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return render_template('test.html')
    else:
        print(request.form['message'])
        if 'message' not in request.form:
            flash('No message in post request', 'error')
            return Response(status=500)
        return jsonify(message=request.form['message'] + ' it is response'), 201

@app.route('/cs/', methods=['GET', 'POST'])
def cs():
    return render_template('cs.html')


if __name__ == '__main__':
    app.run(debug=True)
