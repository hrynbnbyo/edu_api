import xadmin
from xadmin import views
from course.models import CourseCategory, Course, Teacher, CourseChapter, CourseLesson


class CourseCategoryModelAdmin(object):
    pass


xadmin.site.register(CourseCategory, CourseCategoryModelAdmin)


class CourseModelAdmin(object):
    pass


xadmin.site.register(Course, CourseModelAdmin)


class TeacherModelAdmin(object):
    pass


xadmin.site.register(Teacher, TeacherModelAdmin)


class CourseChapterModelAdmin(object):
    pass


xadmin.site.register(CourseChapter, CourseChapterModelAdmin)


class CourseLessonModelAdmin(object):
    pass


xadmin.site.register(CourseLesson, CourseLessonModelAdmin)