from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    occupation = models.CharField(max_length=30,blank=True)
    def __str__(self):
        return self.first_name
    

class Projects(models.Model):
    project_name = models.CharField(max_length=30)
    url = models.URLField(blank=True)
    desc = models.TextField(blank=True)
    user = models.ForeignKey('Person',on_delete=models.CASCADE) 
    def __str__(self):
        return self.project_name