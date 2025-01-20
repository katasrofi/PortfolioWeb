# Django Library
from django.contrib import admin

# My models 
from .models import Profile, Project, Skill, Testimonial

# Customize the admin panel 
class ProjectInLine(admin.StackedInline):
    model = Skill
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
            ('Project Title', {'fields': ['title']}),
            ('More Information', {'fields': ['summary', 'description', 'image', 'url'], 'classes': ['collapse']}),
            ]
    inlines = [ProjectInLine]

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill)
admin.site.register(Testimonial)
