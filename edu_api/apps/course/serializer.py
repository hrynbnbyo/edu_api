from rest_framework.serializers import ModelSerializer

from course.models import CourseCategory, Course, Teacher


class CourseCategoryModelSerializer(ModelSerializer):

    class Meta:
        model = CourseCategory
        fields = ["id", "name"]


class TeacherModelSerializer(ModelSerializer):

    class Meta:
        model = Teacher
        fields = ["id", "name", "title"]


class CourseModelSerializer(ModelSerializer):

    teacher = TeacherModelSerializer()

    class Meta:
        model = Course
        fields = ["id", "name", "course_img", "students", "lessons", "pub_lessons", "price", "teacher", "lesson_list"]


