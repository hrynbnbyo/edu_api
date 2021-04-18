from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter
from course.models import CourseCategory, Course
from course.pagination import CoursePageNumberPagination
from course.serializer import CourseCategoryModelSerializer, CourseModelSerializer


class CourseCategoryView(ListAPIView):
    queryset = CourseCategory.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = CourseCategoryModelSerializer


class CourseListAPIView(ListAPIView):
    queryset = Course.objects.filter(is_show=True, is_delete=False).order_by("-orders")
    serializer_class = CourseModelSerializer

    # 指定过滤使用的模板类
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # 指定要过滤的字段
    filter_fields = ("course_category",)

    # 指定排序的条件
    ordering_fields = ("id", "students", "price")

    # 指定分页器
    pagination_class = CoursePageNumberPagination


class CourseList2APIView(ListAPIView):
    queryset = Course.objects.filter(is_show=True, is_delete=False)
    serializer_class = CourseModelSerializer
