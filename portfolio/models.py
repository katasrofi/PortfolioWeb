from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    social_links = models.URLField(blank=True, 
                                   null=True)

    def __str__(self):
        return self.name 

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
    profile = models.ForeignKey(Profile, 
                                on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)

    # Project parameters
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True, 
                          null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title 


class Testimonial(models.Model):
    name = models.CharField(max_length=60)
    feedback = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    position = models.CharField(max_length=40)

    def __str__(self):
        return self.name 


