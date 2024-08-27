from django.urls import path
from . import views

urlpatterns = [
    path("getColor", views.getColor, name="getColor"),
    path("myColor", views.myColor, name="myColor"),
    path("history", views.viewHistory, name="history"),
    path("setting", views.viewSetting, name="setting"),
    path("colorPalette", views.viewColorPalette, name="colorPalette"),
]