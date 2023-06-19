from django.shortcuts import render,redirect
from django.views import View
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
class Get_started(View):                                 
    def get(self, request) :
        return render(request,'pfapp/Get_started.html')

class Register(View):
    def get(self,request):
        form = NewUserForm()
        return render (request=request, template_name="registration/register.html", context={"register_form":form})
    
    def post(self,request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("pfapp:Get_started")
        messages.error(request, "Unsuccessful registration. Invalid information.")
        return redirect(request.path)