from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    projects = Project.objects.all().order_by('-id')[:18]
    context = {
        'projects':projects
    }
    return render(request, 'index.html', context)


def projects(request):
    projects = Project.objects.all().order_by('-id')
    context = {
        'projects':projects
    }
    return render(request, 'gallery.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')    