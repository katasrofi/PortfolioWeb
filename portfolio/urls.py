# Django Library 
from django.urls import path 

# Views function
from . import views 

# The Urls 
urlpatterns = [
        path('', views.Home.as_view(), name='home')
        ]
