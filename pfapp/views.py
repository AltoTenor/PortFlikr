from django.shortcuts import render,redirect
from django.views import View
from .forms import NewUserForm,DashboardForm,LoginForm,DashboardFormPersonal,DashboardFormProjects,DashboardFormUser
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Person,Projects
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

# Get Started Page.
class Get_started(View):                                 
    def get(self, request) :
        ctx={}
        ctx['rightclass']="d-none d-md-block"
        return render(request,'pfapp/Get_started.html',ctx)


# Register VIEW
class Register(View):
    def get(self,request):
        form = NewUserForm()
        note=request.session.get('note',0)
        if (note):
            del(request.session['note'])
        return render (request=request, template_name="registration/register.html",context={"register_form":form,"leftclass":"d-none d-md-block","note":note})
    
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
        print(form.cleaned_data)
        # print("Error")
        request.session['note'] = 1
        return redirect(request.path)
    

# DASHBOARD VIEW
class Dashboard(LoginRequiredMixin,View):                                 
    def get(self, request) :
        # form = DashboardForm(initial=old_form)
        user_form=DashboardFormUser()
        personal_form=DashboardFormPersonal()
        projects_form=DashboardFormProjects()
        user_info=User.objects.get(username=request.user)
        # print()
        projects=user_info.person.projects_set.all()
        ctx={'user_form':user_form,"personal_form":personal_form,'projects_form':projects_form,"user":user_info,"projects":projects}
        return render(request,'pfapp/dashboard.html',ctx)
    
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
    


#LOGOUT PAGE 
def logout_view(request):
    logout(request)
    messages.success(request,"Logged out successfully.")
    return redirect(reverse_lazy('pfapp:Get_started'))


# PORTFOLIO VIEW
class Portfolio(View):                                 
    def get(self, request , username) :
        return render(request,'pfapp/portfolio.html',{'usr':username})




# LOGIN VIEW
class UpdatedLoginView(LoginView):
    form_class = LoginForm
        
    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']  # get remember me data from cleaned_data of form
        # print(remember_me)
        if not remember_me:
            self.request.session.set_expiry(0)  # if remember me is 
            self.request.session.modified = True
        else:   
            self.request.session.set_expiry(1209600)
        return super(UpdatedLoginView, self).form_valid(form)