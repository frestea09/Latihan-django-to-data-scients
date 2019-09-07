from django.urls import path,re_path,include
from . import views
urlpatterns = [
    re_path(r'^$',views.index),
    re_path(r'^article/$',views.article),
    re_path(r'^jurnal/$',views.jurnal),
    re_path(r'^draf/$',views.draf),
]