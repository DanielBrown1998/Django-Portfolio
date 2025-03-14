from django.shortcuts import render
from home.models import Project

def home(request):
    return render(request, 'home/home.html')

def projects(request):
    projects = Project.objects.all()
    context = {
        "projects": projects,
    }
    return render(request, 'projects/projects.html', context=context)


def card(request, id:int):
    #TODO
    ...
