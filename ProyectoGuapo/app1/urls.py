from django.urls import path

from . import views

app_name = "app1"
urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("mostrar/", views.nada , name="Nose")
]