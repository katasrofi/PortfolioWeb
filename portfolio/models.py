from django.db import models

# Create your models here.
class Skill(models.Model):
    # Skill name 
    name = models.CharField(max_length=50)
    
    # Proficiency 
    PROFICIENCY_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert'),
    ]
    proficiency = models.CharField(max_length=20,
                                   choices=PROFICIENCY_CHOICES)
    
    # Category 
    CATEGORY_CHOICES = [
        ('Programming Language', 'Programming Language'),
        ('Framework', 'Framework'),
        ('Tools', 'Tools'),
        ('Domain', 'Domain'),
    ]
    category = models.CharField(max_length=60,
                                choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name 

class Project(models.Model):
    # Foreign Key
    skills = models.ManyToManyField(Skill)

    # Project parameters
    title = models.CharField(max_length=200)
    summary = models.TextField(null=True,
                               blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True, 
                          null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title 

class Profile(models.Model):
    # Foreign key
    project = models.ManyToManyField(Project) 

    # Profile parameters
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/',
                              blank=True,
                              null=True)
    bio = models.TextField()
    summary = models.TextField(null=True,
                               blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    social_links = models.URLField(blank=True, 
                                   null=True)

    def __str__(self):
        return self.name 


class Testimonial(models.Model):
    name = models.CharField(max_length=60)
    feedback = models.TextField()
    image = models.ImageField(upload_to='images/')
    position = models.CharField(max_length=40)

    def __str__(self):
        return self.name 


