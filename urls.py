from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),  # URL for the index view
    path("add/", views.add, name="add")  # URL for the add view
]
