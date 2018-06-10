from flask import request

from Common.Exceptions import *


class Course:
    @staticmethod
    def getFromForm():
        try:
            return Course(
                request.form['name'],
                'forCS' in request.form,
                'forBA' in request.form,
                request.form['semesterId'],
                request.form['blockId'],
                request.form['description'],
                request.form['prerequisites'],
                request.form['outcomes'],
                request.form['credits'],
                request.form['teacher'],
                'isEnglish' in request.form
            )
        except Exception as e:
            raise FormException(str(e))

    def __init__(
            self,
            name,
            forCS,
            forBA,
            semesterId,
            blockId,
            description,
            prerequisites,
            outcomes,
            credits,
            teacher,
            isEnglish
    ):
        self.name = name
        self.forCS = bool(forCS)
        self.forBA = bool(forBA)
        self.semesterId = int(semesterId)
        self.blockId = int(blockId)
        self.description = description
        self.prerequisites = prerequisites
        self.outcomes = outcomes
        self.credits = float(credits)
        self.teacher = teacher
        self.isEnglish = isEnglish

    def validate(self):
        if len(self.name) == 0:
            raise CourseEmptyNameException("Course Name cannot be empty")
        if not self.forCS and not self.forBA:
            raise CourseLableException("Course should be either for CS or for BA")
        if len(self.description) == 0:
            raise CourseEmptyDescription("Course Description cannot be empty")
        if len(self.prerequisites) == 0:
            raise CourseEmptyPrerequisites("Course Prerequisites cannot be empty")
        if len(self.outcomes) == 0:
            raise CourseEmptyOutcomes("Course Outcomes cannot be empty")
        if len(self.teacher) == 0:
            raise CourseEmptyTeacher("Course Teacher cannot be empty")
