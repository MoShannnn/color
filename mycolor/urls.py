from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("register", views.register, name="register"),
    path("verify-email/<slug:username>", views.verify_email, name="verify-email"),
    path("login", views.login, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("resetPassword", views.forget_password, name="forgotPassword"),
    path("set_password/<uidb64>/<token>/", views.setPassword, name="setPassword"),
]