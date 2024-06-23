from django.contrib.auth import views as authViews
from django.urls import path

from . import views


urlpatterns = [
    path("", views.frontPage, name="frontPage"),
    path("signup/", views.signUp, name="signup"),
    path("logout/", authViews.LogoutView.as_view(), name="logout"),
    path("login/", authViews.LoginView.as_view(template_name='core/login.html'), name="login"),
]   