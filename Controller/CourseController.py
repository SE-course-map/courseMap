from Essence.Course import *
from Connection.Connection import *
from Controller.UpdateController import *


class CourseController(UpdateController):
    @staticmethod
    def add(course):
        course.validate()

        with CourseMapConnection() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """ INSERT INTO course (name, forCS, forBA, blockId, description, prerequisites, outcomes, credits, teacher, isEnglish) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (
                    course.name,
                    course.forCS,
                    course.forBA,
                    course.blockId,
                    course.description,
                    course.prerequisites,
                    course.outcomes,
                    course.credits,
                    course.teacher,
                    course.isEnglish
                )
            )

            cursor.execute("""SELECT * FROM course ORDER BY id DESC LIMIT 1""")
            courseId = int(cursor.fetchone()[0])

            for item in course.semesterId:
                cursor.execute("""SELECT * FROM semester WHERE id=%s""", (item, ))
                if cursor.rowcount() == 0:
                    raise CourseNoSemesters("Wrong value for semester id")

            for item in course.semesterId:
                cursor.execute(
                    """INSERT INTO courseSemester (courseId, semesterId) VALUES (%s, %s)""",
                    (courseId, item)
                )

    @staticmethod
    def remove(courseId):
        with CourseMapConnection() as connection:
            cursor = connection.cursor()
            cursor.execute("""DELETE FROM courseSemester WHERE courseId=%s""", (courseId,))
            cursor.execute("""DELETE FROM course WHERE id=%s""", (courseId, ))

    @staticmethod
    def update(courseId, newCourse):
        newCourse.validate()

        with CourseMapConnection() as connection:
            cursor = connection.cursor()

            for item in newCourse.semesterId:
                cursor.execute("""SELECT * FROM semester WHERE id=%s""", (item, ))
                if cursor.rowcount() == 0:
                    raise CourseNoSemesters("Invalid value for semester")

            cursor.execute(""" UPDATE course SET name=%s, forCS=%s, forBA=%s, blockId=%s, description=%s, prerequisites=%s, outcomes=%s, credits=%s, teacher=%s, isEnglish=%s WHERE id=%s """,
                (
                   newCourse.name,
                   newCourse.forCS,
                   newCourse.forBA,
                   newCourse.blockId,
                   newCourse.description,
                   newCourse.prerequisites,
                   newCourse.outcomes,
                   newCourse.credits,
                   newCourse.teacher,
                   newCourse.isEnglish,
                   courseId
               )
            )

            cursor.execute("""DELETE FROM courseSemester WHERE courseId=%s""", (courseId, ))
            for item in newCourse.semesterId:
                cursor.execute("""INSERT INTO courseSemester (courseId, semesterId) VALUES (%s, %s)""", (courseId, item))

    @staticmethod
    def getAll():
        with CourseMapConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(""" SELECT id, name, forCS, forBA, blockId, description, prerequisites, outcomes, credits, teacher, isEnglish FROM course """)

            resultTmp = cursor.fetchall()
            result = []

            for item in resultTmp:
                item = list(item)
                cursor.execute("""SELECT semesterId FROM courseSemester WHERE courseId=%s""", (item[0] ,))

                relatedSemesters = []
                for relatedSemester in cursor.fetchall():
                    relatedSemesters.append(relatedSemester[0])

                item.append(relatedSemesters)
                result.append(item)

            return tuple(result)
