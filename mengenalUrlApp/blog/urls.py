from django.urls import path,re_path
from . import views as blogViews
urlpatterns=[
    re_path(r'^$',blogViews.index),
]