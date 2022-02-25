from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *

# Create your views here.
def home(request):
    projects = Project.objects.all().order_by('-id')[:18]
    feedbacks = Feedback.objects.all().order_by('-id')[:6]
    partners = Partners.objects.all().order_by('-id')
    context = {
        'projects':projects,
        'feedbacks':feedbacks,
        'partners':partners
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

def feedback(request):
    form = FeedbackForm()
    if request.method == "POST":
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        return redirect('home')      
    context ={
        "form": form
    }

    return render(request, 'feedback.html', context)


def projectDeails(request, id):    
    project = get_object_or_404(Project, id=id)
    context = {
        'project':project
    }
    return render(request, 'project-details.html', context)    


    # Admin VIews

from django.contrib import messages
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

@login_required
def admin(request):
    if request.user.is_staff:
        
        messages = Contact.objects.all().order_by('-id')
        # paginating messages from the contact model
        paginator = Paginator(messages, 4)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # feedbacks
        feedbacks = Feedback.objects.all().order_by('-id')
            # paginating feedbacks from the Feedback model
        paginator = Paginator(feedbacks, 4)

        page_number = request.GET.get('page')
        feedback_obj = paginator.get_page(page_number)

        # paginate projects table
        item_list = Project.objects.all().order_by('-id')
        page = request.GET.get('page', 1)

        paginator = Paginator(item_list, 15)
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)

        form = ProjectsForm()

        if request.method == "POST":
            form = ProjectsForm(request.POST, request.FILES)
            files = request.FILES.getlist('more_project_images')
            if form.is_valid():
                project = form.save()
                for f in files:
                    project_image = ProjectImages(project=project, image=f)
                    project_image.save()

                return redirect('admin')    
        context = {
            'page_obj': page_obj,
            'feedback_obj':feedback_obj,
            'form': form,
            'items':items
        }
        return render(request, 'admin/home.html', context)
    messages.danger(request, "You can't access the admin panel because you are not the admin ")
    return redirect('home')  

def delete_message(request, id):
    message = Contact.objects.get(id=id)
    message.delete()
    return redirect('admin')   


def delete_project(request, id):
    project = Project.objects.get(id=id)
    project.delete()

    return redirect ('admin')

def delete_feedback(request, id):
    feedback = Feedback.objects.get(id=id)
    feedback.delete()

    return redirect ('admin')    


def updateProject(request, id):
    project = Project.objects.get(id=id)
    form = ProjectsForm(instance=project)

    if request.method == "POST":
        form = ProjectsForm(request.POST or None, request.FILES, instance=project)

        if form.is_valid():
            
            form.save()
            return redirect('admin')
    context ={
        'project': project,
        'form': form

    }
    return render(request, 'admin/update-projects.html', context)