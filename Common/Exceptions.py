class DbException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class FormException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class UserControllerException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class PasswordLengthException(UserControllerException):
    def __init__(self, msg):
        super().__init__(msg)


class EmptyUserNameException(UserControllerException):
    def __init__(self, msg):
        super().__init__(msg)


class BlockControllerException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class NameLengthException(BlockControllerException):
    def __init__(self, msg):
        super().__init__(msg)


class ColorLengthException(BlockControllerException):
    def __init__(self, msg):
        super().__init__(msg)


class YearControllerException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class YearPositionException(YearControllerException):
    def __init__(self, msg):
        super().__init__(msg)


class SemesterControllerException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class SemesterPositionException(SemesterControllerException):
    def __init__(self, msg):
        super().__init__(msg)


class SemesterEmptyNameException(SemesterControllerException):
    def __init__(self, msg):
        super.__init__(msg)


class CourseException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class CourseEmptyNameException(CourseException):
    def __init__(self, msg):
        super().__init__(msg)


class CourseLableException(CourseException):
    def __init__(self, msg):
        super().__init__(msg)


class CourseEmptyDescription(CourseException):
    def __init__(self, msg):
        super().__init__(msg)


class CourseEmptyPrerequisites(CourseException):
    def __init__(self, msg):
        super().__init__(msg)


class CourseEmptyOutcomes(CourseException):
    def __init__(self, msg):
        super().__init__(msg)


class CourseEmptyTeacher(CourseException):
    def __init__(self, msg):
        super().__init__(msg)