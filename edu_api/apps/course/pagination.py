from rest_framework.pagination import PageNumberPagination


class CoursePageNumberPagination(PageNumberPagination):
    page_query_param = "page"
    page_size = 2
    page_size_query_param = "size"
    max_page_size = 10
