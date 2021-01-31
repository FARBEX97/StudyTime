from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from users.models import Project, Category, Session, Milestone
from users.views import charts


DETAIL_VIEWS_PATH = 'users/views/detail_views/'


def category_dashboard(request, project, category):
    if request.user.is_authenticated:
        try:
            category = Category.objects.get(user=request.user, category_name=category)
            chart = charts.category_chart(Session.objects.filter(category=category))
        except:
            category = Category()
            return redirect('/')
    else:
        return redirect('user_not_logged_in')


    context = {
        "project": project,
        "category": category,
        "chart": chart,
    }

    return render(request, DETAIL_VIEWS_PATH + 'category_dashboard.html', context)


def category_sessions(request, project, category):
    if request.user.is_authenticated:
        try:
            project = Project.objects.get(user=request.user, project_name=project)
            category = Category.objects.get(user=request.user, category_name=category)
            sessions = Session.objects.filter(category=category)

        except:
            category = Category()
            return redirect('/')
    else:
        return redirect('user_not_logged_in')


    print(category)

    context = {
        "project": project,
        "category": category,
        "sessions": sessions,
    }

    return render(request, DETAIL_VIEWS_PATH + 'category_sessions.html', context)


def category_milestones(request, project, category):
    if request.user.is_authenticated:
        try:
            project = Project.objects.get(user=request.user, project_name=project)
            category = Category.objects.get(user=request.user, category_name=category)
            milestones = Milestone.objects.filter(category=category)
        except:
            category = Category()
            return redirect('/')
    else:
        return redirect('user_not_logged_in')


    context = {
        "project": project,
        "category": category,
        "milestones": milestones,
    }

    return render(request, DETAIL_VIEWS_PATH + 'category_milestones.html', context)