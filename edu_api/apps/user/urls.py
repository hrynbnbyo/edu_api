from django.urls import path
from rest_framework_jwt import views
from user import views as views2

urlpatterns = [
    path("login/", views.obtain_jwt_token),
    path("login2/", views2.PhoneLoginAPIView.as_view()),
    path("captcha/", views2.CaptchaAPIView.as_view()),
    path("register/", views2.UserAPIView.as_view()),
    path("message/", views2.SendMessageAPIView.as_view()),
]