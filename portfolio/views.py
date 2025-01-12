# Django Library
from django.shortcuts import render
from django.views import generic

# Models
from .models import Profile, Project, Skill, Testimonial

# Create your views here.
class Home(generic.ListView):
    model = Profile
    template_name = 'portfolio/home.html'
    context_object_name = 'profile'

    def get_queryset(self):
        return super().get_queryset()


