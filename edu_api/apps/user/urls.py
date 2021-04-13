from django.urls import path
from rest_framework_jwt import views
from user import views as views2

urlpatterns = [
    path("login/", views.obtain_jwt_token),
    path("captcha/", views2.CaptchaAPIView.as_view()),
]