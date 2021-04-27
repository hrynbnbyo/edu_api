from django.urls import path

from course import views

urlpatterns = [
    path("category/", views.CourseCategoryView.as_view()),
    path("course_list/", views.CourseListAPIView.as_view()),
    path("course_detail/", views.CourseDetailsAPIView.as_view()),
]