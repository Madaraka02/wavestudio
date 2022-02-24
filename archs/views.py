from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *

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
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact')
        return redirect('home')      
    context ={
        "form": form
    }

    return render(request, 'contact.html', context)    


def projectDeails(request, id):    
    project = get_object_or_404(Project, id=id)
    context = {
        'project':project
    }
    return render(request, 'project-details.html', context)    