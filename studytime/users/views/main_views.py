from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import CustomUserCreationForm
from users.models import Project, Category


MAIN_VIEWS_PATH = 'users/views/'


def home(request):
    return redirect('project_listview')


def register(request):
    if request.method == 'GET':
        return render(
            request, 'registration/register.html',
            {'form': CustomUserCreationForm}
        )
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('project_listview')


def user_not_logged_in(request):

    return render(request, 'user_not_logged_in.html')


def project_listview(request):

    projects = []
    if request.user.is_authenticated:
        projects = Project.objects.filter(user=request.user)
    else:
        return redirect('user_not_logged_in')
   
    
    context = {
        "projects": projects,
    }

    return render(request, MAIN_VIEWS_PATH + 'project_listview.html', context)


def category_listview(request, project):

    categories = []
    if request.user.is_authenticated:
        project = Project.objects.get(user=request.user, project_name=project)
        categories = Category.objects.filter(user=request.user, project=project)

    else:
        return redirect('user_not_logged_in')
    
    context = {
        "project": project,
        "categories": categories,
    }

    return render(request, MAIN_VIEWS_PATH + 'category_listview.html', context)


def help_view(request):
    return render(request, MAIN_VIEWS_PATH + 'help_view.html')
