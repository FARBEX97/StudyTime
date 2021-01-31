from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Form, ModelChoiceField, CharField, DateField, IntegerField, widgets, SelectDateWidget
from users.models import Project, Category, Session, Milestone

from django.db import models
from django.contrib.auth.models import User



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user',User())
        super(ProjectCreationForm, self).__init__(*args, **kwargs)
        self.fields['project_name'] = CharField(max_length=200)



class ProjectDeletionForm(Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user',User())
        super(ProjectDeletionForm, self).__init__(*args, **kwargs)
        self.fields['project_name'] = ModelChoiceField(Project.objects.filter(user=user), initial=0)


    

class CategoryCreationForm(ModelForm):
    # Instanciate Category loading every project of an empty User()
    # Then replace User() with request.user in views.py
    # https://stackoverflow.com/questions/5708650/how-do-i-add-a-foreign-key-field-to-a-modelform-in-django
    class Meta:
        model = Category
        exclude = ['project', 'user']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user',User())
        super(CategoryCreationForm, self).__init__(*args, **kwargs)
        self.fields['category_name'] = CharField(max_length=200)


class CategoryDeletionForm(Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user',User())
        project = kwargs.pop('project',Project())
        super(CategoryDeletionForm, self).__init__(*args, **kwargs)
        self.fields['category_name'] = ModelChoiceField(Category.objects.filter(user=user, project=project), initial=0)



class SessionCreationForm(ModelForm):
    class Meta:
        model = Session
        exclude = ['project', 'category', 'user']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user',User())
        super(SessionCreationForm, self).__init__(*args, **kwargs)
        self.fields['session_date'] = DateField(
            widget=widgets.DateInput(attrs={'type': 'date'})
        )
        self.fields['session_time'] = IntegerField()



class MilestoneCreationForm(ModelForm):
    class Meta:
        model = Milestone
        exclude = ['user', 'project', 'category']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user',User())
        super(MilestoneCreationForm, self).__init__(*args, **kwargs)
        self.fields['milestone_title'] = CharField(max_length=200)
        self.fields['milestone_date'] = DateField(
            widget=widgets.DateInput(attrs={'type': 'date'})
        )
        self.fields['milestone_description'] = CharField(max_length=500)



class MilestoneEditForm(Form):

    def __init__(self, *args, **kwargs):
        milestone = kwargs.pop('milestone',Milestone())
        super(MilestoneEditForm, self).__init__(*args, **kwargs)
        self.fields['milestone_title'] = CharField(max_length=200, initial=milestone.milestone_title)
        self.fields['milestone_date'] = DateField(
            widget=widgets.DateInput(attrs={'type': 'date'}), initial=milestone.milestone_date
        )
        self.fields['milestone_description'] = CharField(max_length=500, initial=milestone.milestone_description)
        passed_milestone = True
