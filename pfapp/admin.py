from django.contrib import admin
from .models import Person,Projects,Work

# Register your models here.

admin.site.register(Person)
admin.site.register(Projects)
admin.site.register(Work)