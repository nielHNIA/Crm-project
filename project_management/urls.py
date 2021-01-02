from django.urls import path, include

from . import views

app_name = 'project_management'



urlpatterns = [

 path('project/', views.project, name = 'project'),
 path('project_detail', views.project_detail, name='project_detail'),
 path('clients', views.clients, name='clients'),
 path('client', views.client, name='client'),
 path('contractors', views.contractors, name='contractors'),
 path('contractor', views.contractor, name='contractor'),
 path('reports', views.reports, name='reports'),
 path('report', views.report, name='report'),
 path('sites', views.sites, name='sites'),
 path('site', views.site, name='site'),
 path('teams', views.teams, name='teams'),
 path('team', views.team, name='team'),

]
