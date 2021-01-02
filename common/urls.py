from django.urls import path

from . import views
app_name = 'common'

urlpatterns = [
  path('', views.index, name='index'),
  path('home/', views.home, name='home'),
  path('profile/', views.view_profile, name='profile'),
  path('top_bar/', views.top_bar, name='top_bar'),
  path('sidebar/', views.sidebar, name='sidebar')
]
