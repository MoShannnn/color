from django.urls import path
from . import views

urlpatterns = [
    path("getColor", views.getColor, name="getColor"),
    # path("myColor", views.myColor, name="myColor"),
    path("history", views.viewHistory, name="history"),
    path("style", views.viewStyle, name="style"),
    path("setting", views.viewSetting, name="setting"),
    path('deleteImage/<int:id>', views.deleteImage, name="deleteImage"),
    
    path("colorPalette", views.viewColorPalette, name="colorPalette"),
]