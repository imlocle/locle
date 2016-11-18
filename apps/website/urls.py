from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^finder', views.finder),
    url(r'^writenow', views.writenow),
    url(r'^guilty', views.guilty),
]
