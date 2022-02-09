from django.urls import path
from django.conf.urls import patterns, include, url

from . import views

app_name = "app1"
urlpatterns = patterns(
    url("", views.index)
)