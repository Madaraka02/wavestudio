from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')


def projects(request):
    return render(request, 'projects.html')
