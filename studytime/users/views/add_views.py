from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from users.forms import ProjectCreationForm, CategoryCreationForm, SessionCreationForm, MilestoneCreationForm
from users.models import Project, Category, Session, Milestone

ADD_VIEWS_PATH = 'users/views/add_views/'



def add_project_form(request):
    if request.user.is_authenticated:
        if request.method == 'POST':

            newprojectform = ProjectCreationForm(request.POST, user=request.user)

            if newprojectform.is_valid():
                project_name = newprojectform.cleaned_data.get('project_name')
                newproject = Project(user=request.user, project_name=project_name)
                try:
                    newproject.save()
                except:
                    pass
                return redirect('/')

        else:
            newprojectform = ProjectCreationForm()

    else:
        return redirect('user_not_logged_in')

    context = {
        "newprojectform": newprojectform,
    }
    return render(request, ADD_VIEWS_PATH + 'add_project_view.html', context)



def add_category_form(request, project):
    if request.user.is_authenticated:
        
        if request.method == 'POST':

            newcategoryform = CategoryCreationForm(request.POST, user=request.user)

            if newcategoryform.is_valid():
                # Used cleaned data to extract the selected project and users input on category_name
                # Then create an instance of Category using both of them and save the instance into DB.
                category_name = newcategoryform.cleaned_data.get('category_name')
                project = Project.objects.get(user=request.user, project_name=project)
                newcategory = Category(
                    user=request.user,
                    project=project,
                    category_name=category_name
                    )
                try:
                    newcategory.save()
                except:
                    pass

                return redirect('..')

        else:
            newcategoryform = CategoryCreationForm(user=request.user)

    else:
        return redirect('user_not_logged_in')


    context = {
        "newcategoryform": newcategoryform,
        "project": project,
    }
    return render(request, ADD_VIEWS_PATH + 'add_category_view.html', context)



def add_session_form(request, project, category):
    if request.user.is_authenticated:
        try:
            category = Category.objects.get(user=request.user, category_name=category)
        except:
            category = Category()
            return redirect('/')

        if request.method == 'POST':
            newsessionform = SessionCreationForm(request.POST, user=request.user)

            if newsessionform.is_valid():
                selected_project = newsessionform.cleaned_data.get('project')
                project = category.project
                session_date = newsessionform.cleaned_data.get('session_date')
                session_time = newsessionform.cleaned_data.get('session_time')
                newsession = Session(
                    user=request.user,
                    project=project,
                    category=category,
                    session_date=session_date,
                    session_time=session_time
                    )
                newsession.save()

                return redirect('..')

        else:
            newsessionform = SessionCreationForm(user=request.user)

    else:
        return redirect('user_not_logged_in')


    context = {
        "newsessionform": newsessionform,
        "project": project,
        "category": category,
    }
    return render(request, ADD_VIEWS_PATH + 'add_session_view.html', context)



def add_milestone_form(request, project, category):
    if request.user.is_authenticated:
        try:
            category = Category.objects.get(user=request.user, category_name=category)
        except:
            category = Category()
            return redirect('/')

        if request.method == 'POST':
            newmilestoneform = MilestoneCreationForm(request.POST, user=request.user)

            if newmilestoneform.is_valid():
                selected_project = newmilestoneform.cleaned_data.get('project')
                project = category.project
                milestone_title = newmilestoneform.cleaned_data.get('milestone_title')
                milestone_date = newmilestoneform.cleaned_data.get('milestone_date')
                milestone_description = newmilestoneform.cleaned_data.get('milestone_description')
                newmilestone = Milestone(
                    user=request.user,
                    project=project,
                    category=category,
                    milestone_title=milestone_title,
                    milestone_date=milestone_date,
                    milestone_description=milestone_description
                    )
                try:
                    newmilestone.save()
                except:
                    pass

                return redirect('..')

        else:
            newmilestoneform = MilestoneCreationForm(user=request.user)
    
    else:
        return redirect('user_not_logged_in')

    context = {
        "newmilestoneform": newmilestoneform,
        "project": project,
        "category": category,
    }
    return render(request, ADD_VIEWS_PATH + 'add_milestone_view.html', context)
