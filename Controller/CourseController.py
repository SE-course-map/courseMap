from Essence.Course import *
from Connection.Connection import *


class CourseController:
    @staticmethod
    def add(course):
        course.validate()

        with CourseMapConnection() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """ INSERT INTO course (name, forCS, forBA, semesterId, blockId, description, prerequisites, outcomes, credits, teacher, isEnglish) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (
                    course.name,
                    course.forCS,
                    course.forBA,
                    course.semesterId,
                    course.blockId,
                    course.description,
                    course.prerequisites,
                    course.outcomes,
                    course.credits,
                    course.teacher,
                    course.isEnglish
                )
            )

    @staticmethod
    def remove(courseId):
        with CourseMapConnection() as connection:
            cursor = connection.cursor()
            cursor.execute("""DELETE FROM course WHERE id=%s""", (courseId, ))

    @staticmethod
    def update(courseId, newCourse):
        newCourse.validate()

        with CourseMapConnection() as connection:
            cursor = connection.cursor()

            cursor.execute(""" UPDATE course SET name=%s, forCS=%s, forBA=%s, semesterId=%s, blockId=%s, description=%s, prerequisites=%s, outcomes=%s, credits=%s, teacher=%s, isEnglish=%s WHERE id=%s """,
                (
                   newCourse.name,
                   newCourse.forCS,
                   newCourse.forBA,
                   newCourse.semesterId,
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

    @staticmethod
    def getAllCourseInfo():
        with CourseMapConnection() as connection:
            cursor = connection.cursor()
            cursor.execute(""" SELECT id, name, forCS, forBA, semesterId, blockId, description, prerequisites, outcomes, credits, teacher, isEnglish FROM course """)
            return cursor.fetchall()
