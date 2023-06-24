from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Person(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) 
    occupation = models.CharField(max_length=30,blank=True)
    def __str__(self):
        return self.user.first_name
    

class Projects(models.Model):
    project_name = models.CharField(max_length=30)
    url = models.URLField(blank=True)
    desc = models.TextField(blank=True)
    person = models.ForeignKey('Person',on_delete=models.CASCADE) 
    def __str__(self):
        return self.project_name