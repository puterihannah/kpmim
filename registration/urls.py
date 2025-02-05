from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("course/", views.course, name="course"),
    path("index/", views.index, name="homepage"),
    path('mentor/', views.mentor, name='mentor'),
    path('searchcourse/', views.searchcourse, name='searchcourse'),
    path('course/updateCourse/', views.searchcourse, name='updateCourse'),
    path('course/updateCourse/', views.searchcourse, name='updateCourse'),
]