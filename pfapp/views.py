from django.shortcuts import render
from django.views import View

# Create your views here.
class Get_started(View):                                 
    def get(self, request) :
        return render(request,'pfapp/Get_started.html')