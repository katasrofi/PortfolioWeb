# Django Library
from django.contrib import admin

# My models 
from .models import Profile, Project, Skill, Testimonial

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Testimonial)
