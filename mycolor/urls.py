from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("register", views.register, name="register"),
    path("verify-email/<slug:username>", views.verify_email, name="verify-email"),
    path("login", views.login, name="login"),
    path("searchEmail", views.searchEmail, name="searchEmail"),
    path("forgotPassword", views.forgotPassword, name="forgotPassword"),
]