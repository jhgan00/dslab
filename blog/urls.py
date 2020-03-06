"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from mysite.views import HomeView
from blog.views import *

app_name = 'blog'
urlpatterns = [
    path('', BlogPostLV.as_view(), name='index'),
    path('post/', BlogPostLV.as_view(), name='post_list'),
    re_path(r'^post/(?P<slug>[-\w]+)/$', BlogPostDV.as_view(), name='post_detail'),
    path('archive/', BlogPostAV.as_view(), name='post_archive'),
    path('archive/<int:year>/', BlogPostYAV.as_view(), name='post_archive_year'),
    path('archive/<int:year>/<str:month>', BlogPostMAV.as_view(), name='post_archive_month'),
    path('archive/<int:year>/<str:month>/<int:day>', BlogPostDAV.as_view(), name='post_archive_day'),
    path('today', BlogPostTAV.as_view(), name='post_archive_today'),
]
