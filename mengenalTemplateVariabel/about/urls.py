from django.urls import path,re_path
from . import views as viewsAbout
urlpatterns=[
    re_path(r'^$',viewsAbout.index),
]