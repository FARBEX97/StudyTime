from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from users.forms import MilestoneEditForm
from users.models import Project, Category, Milestone


EDIT_VIEWS_PATH = 'users/views/edit_views/'



def edit_milestone_form(request, project, category, milestone):
    if request.user.is_authenticated:
        project = Project.objects.get(user=request.user, project_name=project)
        category = Category.objects.get(user=request.user, project=project, category_name=category)
        milestone = Milestone.objects.get(user=request.user, project=project, category=category, milestone_title=milestone)

        if request.method == 'POST':
            editmilestoneform = MilestoneEditForm(request.POST, milestone=milestone)

            if editmilestoneform.is_valid():
                edited_milestone_title = editmilestoneform.cleaned_data.get('milestone_title')
                edited_milestone_date = editmilestoneform.cleaned_data.get('milestone_date')
                edited_milestone_description = editmilestoneform.cleaned_data.get('milestone_description')
                milestone.milestone_title = edited_milestone_title
                milestone.milestone_date = edited_milestone_date
                milestone.milestone_description = edited_milestone_description
                try:
                    milestone.save()
                except:
                    pass

                return redirect('../..')

        else:
            editmilestoneform = MilestoneEditForm(milestone=milestone)
    
    else:
        return redirect('user_not_logged_in')

    context = {
        "editmilestoneform": editmilestoneform,
        "milestone": milestone,
    }
    return render(request, EDIT_VIEWS_PATH + 'edit_milestone_view.html', context)
