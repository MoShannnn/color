from django.urls import path
from . import views

urlpatterns = [
    path("getColor", views.getColor, name="getColor"),
]