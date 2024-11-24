from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views as homeViews

urlpatterns = [
    path("", homeViews.home)
]
