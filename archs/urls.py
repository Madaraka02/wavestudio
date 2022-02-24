from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('projects/', projects, name="projects"),
    path('projects/<int:id>/', projectDeails, name="project"),
    path('contact-us/', contact, name="contact"),
    path('feedback/', feedback, name="feedback"),
]