# Django Library 
from django.urls import path 

# Views function
from . import views 

# App name 
app_name = 'portfolio'

# The Urls 
urlpatterns = [
        path('', views.Home.as_view(), name='home'),
        path('project/<int:pk>/', views.ProjectPortfolio.as_view(), name='project'),
        #path('project/<int:pk>/', views.ProjectPage, name='project'),

        ]
