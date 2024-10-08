from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("aboutUs", views.aboutUs, name="aboutUs"),
    path("contactUs", views.contactUs, name="contactUs"),
    path("register", views.register, name="register"),
    path("verify-email/<uuid:user_uuid>/", views.verify_email, name="verify-email"),
    path("login", views.login, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("deleteAccount", views.deleteAccount, name="deleteAccount"),
    path("resetPassword", views.forget_password, name="forgotPassword"),
    path("set_password/<uidb64>/<token>/", views.setPassword, name="setPassword"),
]