from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from users.forms import ProjectDeletionForm, CategoryDeletionForm
from users.models import Project, Category, Session, Milestone


DEL_VIEWS_PATH = 'users/views/del_views/'


def del_project_form(request):
    if request.user.is_authenticated:
        if request.method == 'POST':

            delprojectform = ProjectDeletionForm(request.POST, user=request.user)

            if delprojectform.is_valid():
                project_name = delprojectform.cleaned_data.get('project_name')
                delproject = Project.objects.get(user=request.user, project_name=project_name)
                delproject.delete()

                return redirect('/')

        else:
            delprojectform = ProjectDeletionForm(user=request.user)

    else:
        return redirect('user_not_logged_in')

    context = {
        "delprojectform": delprojectform,
    }
    return render(request, DEL_VIEWS_PATH + 'del_project_view.html', context)



def del_category_form(request, project):
    if request.user.is_authenticated:
        project = Project.objects.get(user=request.user, project_name=project)
        if request.method == 'POST':

            delcategoryform = CategoryDeletionForm(request.POST, user=request.user, project=project)

            if delcategoryform.is_valid():
                category_name = delcategoryform.cleaned_data.get('category_name')
                delcategory = Category.objects.get(user=request.user, project=project, category_name=category_name)
                delcategory.delete()

                return redirect('./../c')

        else:
            delcategoryform = CategoryDeletionForm(user=request.user, project=project)

    else:
        return redirect('user_not_logged_in')

    context = {
        "delcategoryform": delcategoryform,
    }
    return render(request, DEL_VIEWS_PATH + 'del_category_view.html', context)
