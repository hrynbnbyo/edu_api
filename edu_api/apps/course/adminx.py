import xadmin
from xadmin import views
from course.models import CourseCategory, Course, Teacher, CourseChapter, CourseLesson, CourseDiscountType, \
    CourseDiscount, Activity, CoursePriceDiscount, CourseExpire


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

# 以下是优惠活动相关


class PriceDiscountTypeModelAdmin(object):
    """价格优惠类型"""
    pass


xadmin.site.register(CourseDiscountType, PriceDiscountTypeModelAdmin)


class PriceDiscountModelAdmin(object):
    """价格优惠公式"""
    pass


xadmin.site.register(CourseDiscount, PriceDiscountModelAdmin)


class CoursePriceDiscountModelAdmin(object):
    """商品优惠和活动的关系"""
    pass


xadmin.site.register(CoursePriceDiscount, CoursePriceDiscountModelAdmin)


class ActivityModelAdmin(object):
    """商品活动模型"""
    pass


xadmin.site.register(Activity, ActivityModelAdmin)


xadmin.site.register(CourseExpire)