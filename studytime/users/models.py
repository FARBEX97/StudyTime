from django.db import models
from django.contrib.auth.models import User



# User model modified
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone

class Project(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Projects"
        constraints = [
            models.UniqueConstraint(fields=['user', 'project_name'], name='unique project_name')
        ]

    def __str__(self):
        return self.project_name


class Category(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    project = models.ForeignKey(Project, verbose_name="Project", on_delete=models.CASCADE)
    category_name = models.CharField(max_length=200)
    

    class Meta:
        verbose_name_plural = "Categories"
        constraints = [
            models.UniqueConstraint(fields=['user', 'project', 'category_name'], name='unique category_name')
        ]


    def __str__(self):
        return self.category_name


    def get_total_time(self):
        category_totaltime = 0
        category_sessions = Session.objects.filter(category=self)
        for session in category_sessions:
                category_totaltime += session.session_time
        return category_totaltime

    
    def get_total_sessions(self):
        category_sessions = Session.objects.filter(category=self)
        return len(category_sessions)


    def get_first_session_date(self):
        try:
            return Session.objects.filter(category=self).first().session_date
        except AttributeError:
            return False
    

    def get_last_session_date(self):
        try:
            return Session.objects.filter(category=self).last().session_date
        except AttributeError:
            return False


    def get_last_milestone_title(self):
        try:
            return Milestone.objects.filter(category=self).last().milestone_title
        except AttributeError:
            return False


    def get_last_milestone_date(self):
        try:
            return Milestone.objects.filter(category=self).last().milestone_date
        except AttributeError:
            return False




class Session(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    project = models.ForeignKey(Project, verbose_name="Project", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, default=1, verbose_name="Category", on_delete=models.CASCADE)
    session_date = models.DateField()
    session_time = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Sessions"

    def __str__(self):
        return str(self.session_date) + " session"


class Milestone(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    project = models.ForeignKey(Project, verbose_name="Project", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, default=1, verbose_name="Category", on_delete=models.CASCADE)
    milestone_title = models.CharField(max_length=200)
    milestone_date = models.DateField()
    milestone_description = models.CharField(max_length=500)
    
    class Meta:
        verbose_name_plural = "Milestones"
        constraints = [
            models.UniqueConstraint(fields=['user', 'project', 'category', 'milestone_title'], name='unique milestone_title')
        ]

    def __str__(self):
        return self.milestone_title

