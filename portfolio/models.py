from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    social_links = models.URLField(blank=True, 
                                   null=True)

    def __str__(self):
        return self.name 

class Project(models.Model):
    profile = models.ForeignKey(Profile, 
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=600)
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True, 
                          null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title 

class Skill(models.Model):
    project = models.ForeignKey(Project, 
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    proficiency = models.CharField(max_length=20)
    category = models.CharField(max_length=60)

    def __str__(self):
        return self.name 

class Testimonial(models.Model):
    name = models.CharField(max_length=60)
    feedback = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    position = models.CharField(max_length=40)

    def __str__(self):
        return self.name 


