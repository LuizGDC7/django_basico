from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views as blogViews

urlpatterns = [
    path('', blogViews.blog),
    path('sub/', blogViews.subsubBlog)
]