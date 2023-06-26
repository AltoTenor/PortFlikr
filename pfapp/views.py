from django.shortcuts import render,redirect
from django.views import View
from .forms import NewUserForm,DashboardForm,LoginForm
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Person,Projects
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

# Create your views here.
class Get_started(View):                                 
    def get(self, request) :
        ctx={}
        ctx['rightclass']="d-none d-md-block"
        return render(request,'pfapp/Get_started.html',ctx)

class Register(View):
    def get(self,request):
        form = NewUserForm()
        return render (request=request, template_name="registration/register.html",context={"register_form":form,"leftclass":"d-none d-md-block"})
    
    def post(self,request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            user_info = User.objects.get(username=user)
            person_info=Person(user=user_info)
            person_info.save()


            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("pfapp:dashboard")
        messages.error(request, "Unsuccessful registration. Invalid information.")
        # print("Error")
        return redirect(request.path)
    


class Dashboard(LoginRequiredMixin,View):                                 
    def get(self, request) :
        old_form=request.session.get('old_form',{})
        form = DashboardForm(initial=old_form)
        if (old_form):
            del(request.session['old_form'])
        return render(request,'pfapp/dashboard.html',{'form':form})
    
    def post(self,request):
        form=DashboardForm(request.POST)

        if form.is_valid():
            formcleaned=form.cleaned_data
            user_info = User.objects.get(username=request.user)

            # Adding Occupation
            person_info=Person.objects.filter(user=user_info)
            if (formcleaned['occupation']!=''):
                person_info.update(occupation=formcleaned['occupation'])

            #Adding Project Details
            person_obj=Person.objects.get(user=user_info)
            person_obj.projects_set.create(project_name=formcleaned['project_name'],url=formcleaned['url'],desc=formcleaned['desc'])

        else:
            
            request.session['old_form']=form.cleaned_data
            return redirect(request.path)
        # print(form.cleaned_data)
        return redirect(reverse_lazy('pfapp:Get_started'))
    

def logout_view(request):
    logout(request)
    messages.success(request,"Logged out successfully.")
    return redirect(reverse_lazy('pfapp:Get_started'))

class Portfolio(View):                                 
    def get(self, request , username) :
        return render(request,'pfapp/portfolio.html',{'usr':username})


class UpdatedLoginView(LoginView):
    form_class = LoginForm
    
    def form_valid(self, form):
       
        remember_me = form.cleaned_data['remember_me']  # get remember me data from cleaned_data of form
        print(remember_me)
        if not remember_me:
            self.request.session.set_expiry(0)  # if remember me is 
            self.request.session.modified = True
        return super(UpdatedLoginView, self).form_valid(form)