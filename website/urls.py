from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('courses.html', views.courses, name="courses"),
]