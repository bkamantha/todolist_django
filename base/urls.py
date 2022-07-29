from nturl2path import url2pathname
from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.taskList, name='tasklist')
]
