from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('projects/', projects, name="projects"),
    path('projects/<int:id>/', projectDeails, name="project"),
    path('contact-us/', contact, name="contact"),
    path('feedback/', feedback, name="feedback"),

   
    path('wavegridadmin/', admin, name='admin'),
    path('update/<int:id>/', updateProject, name='update_project'),
    path('delete-message/<int:id>/', delete_message, name="delete-message"),
    path('delete-project/<int:id>/', delete_project, name="delete-project"),
    path('delete-feedback/<int:id>/', delete_feedback, name="delete-feedback"),
]