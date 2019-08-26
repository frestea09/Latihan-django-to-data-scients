from django.urls import path,re_path
from . import views as aboutViews
urlpatterns=[
    path('index/',aboutViews.index),
    re_path(r'^$',aboutViews.index),
]