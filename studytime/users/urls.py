from django.urls import include, path
from users.views.main_views import home, register, user_not_logged_in, category_listview, project_listview, help_view
from users.views.add_views import add_project_form, add_category_form, add_milestone_form, add_session_form
from users.views.del_views import del_project_form, del_category_form
from users.views.edit_views import edit_milestone_form
from users.views.detail_views import category_dashboard, category_milestones, category_sessions


urlpatterns = [
    path('user_not_logged_in/', user_not_logged_in, name='user_not_logged_in'),
    path('register/', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('help/', help_view, name='help'),

    # Project and category dashboards
    path('', home, name='home'),
    path('p/', project_listview, name='project_listview'),
    path('p/<project>/c/', category_listview, name='category_listview'),

    # addforms
    path('p/add_project/', add_project_form, name='add_project'),
    path('p/del_project/', del_project_form, name='del_project'),
    path('p/<project>/c/add_category/', add_category_form, name='add_category'),
    path('p/<project>/c/del_category/', del_category_form, name='del_category'),

    # category detail
    path('p/<project>/c/<category>/dashboard/', category_dashboard, name='category_dashboard'),
    path('p/<project>/c/<category>/sessions/', category_sessions, name='category_sessions'),
    path('p/<project>/c/<category>/milestones/', category_milestones, name='category_milestones'),
    path('p/<project>/c/<category>/sessions/new/', add_session_form, name='add_session_form'),
    path('p/<project>/c/<category>/milestones/new/', add_milestone_form, name='add_milestone_form'),
    path('p/<project>/c/<category>/milestones/<milestone>/edit/', edit_milestone_form, name='edit_milestone'),
]