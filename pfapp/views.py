from django.shortcuts import render,redirect
from django.views import View
from .forms import NewUserForm
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

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
            return redirect("pfapp:dashboard")
        messages.error(request, "Unsuccessful registration. Invalid information.")
        # print("Error")
        return redirect(request.path)
    


class Dashboard(LoginRequiredMixin,View):                                 
    def get(self, request) :
        return render(request,'pfapp/dashboard.html')
    

def logout_view(request):
    logout(request)
    messages.success(request,"Logged out successfully. ")
    return redirect(reverse_lazy('pfapp:Get_started'))

class Portfolio(View):                                 
    def get(self, request , username) :
        return render(request,'pfapp/portfolio.html',{'usr':username})
