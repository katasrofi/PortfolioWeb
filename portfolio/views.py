# Django Library
from django.shortcuts import render
from django.views import generic

# Models
from .models import Profile, Project, Skill, Testimonial

# Create your views here.
#def HomePage(request):
#    template = 'portfolio/home.html'
#    profiles = Profile.objects.first()
#    context = {'profiles': profiles}
#    return render(request, template, context)
#
# Works but kinda obselete
class Home(generic.DetailView):
    model = Profile
    template_name = 'portfolio/home.html'
    context_object_name = 'profiles'

    def get_object(self, queryset=None):
        return Profile.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context 

def ProjectPage(request, pk):
    template = 'portfolio/project_detail.html'
    projects = Project.objects.filter(id=pk).first()
    context = {'projects': projects}
    return render(request, template, context)

class ProjectPortfolio(generic.DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'projects'

