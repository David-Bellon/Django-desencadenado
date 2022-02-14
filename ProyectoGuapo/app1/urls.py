from django.urls import path

from . import views

app_name = "app1"
urlpatterns = [
    path("", views.index, name="index"),
    path("forum/", views.render_forum),
    path("forum/search/", views.search, name="search"),
    path("sign_up/", views.nada , name="Nose")
]