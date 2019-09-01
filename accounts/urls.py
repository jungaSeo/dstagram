from django.urls import path, include
from django.contrib.auth import views as auth_view

from .views import register

urlpatterns = [
    # 로그인 뷰 연결
    path('login/', auth_view.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # 로그아웃 뷰 연결
    path('logout/', auth_view.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    # 회원가입 뷰 연결
    path('register/', register, name='register'),
]