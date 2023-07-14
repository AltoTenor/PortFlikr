from django.shortcuts import render,redirect
from django.views import View
from .forms import NewUserForm,LoginForm,DashboardFormPersonal,DashboardFormProjects,DashboardFormUser, DashboardFormWork
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Person,Projects
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseNotFound
from rest_framework import permissions,viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .serializer import Personserializer


# from . serializer import *

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
        #FORMS

        user_form=DashboardFormUser()
        personal_form=DashboardFormPersonal()
        projects_form=DashboardFormProjects()
        work_form=DashboardFormWork()

        #Information
        user_info=User.objects.get(username=request.user)
        projects=user_info.person.projects_set.all()
        workexp=user_info.person.work_set.all()

        ctx={'user_form':user_form,"personal_form":personal_form,'projects_form':projects_form,'work_form':work_form,"user":user_info,"projects":projects,"works":workexp}
        return render(request,'pfapp/dashboard.html',ctx)
    
    def post(self,request):
        #Portfolio Call
        if (request.POST.get('portfolio-style')!=None):
            # return HttpResponseNotFound("Still in development coming soon")
            # return redirect("http://localhost:3000")
            return redirect("https://portflikr.web.app/"+str(request.POST.get('portfolio-style'))+"/"+str(request.user.pk-1))

 

class Profile(View):
    def post(self,request):
        #Forms and cleaning
        form1=DashboardFormUser(request.POST, request.FILES)
        form2=DashboardFormPersonal(request.POST, request.FILES)
        print(form2)
        form1.is_valid()
        form2.is_valid()
        cleaned1=form1.cleaned_data
        cleaned2=form2.cleaned_data

        # print("In Profile View ")
        # print(cleaned1)
        # print(cleaned2)

        # Handling Data
        print(cleaned2)
        if 'img' in cleaned2:
            request.user.person.img=cleaned2['img']
        if 'img1' in cleaned2:
            request.user.person.img1=cleaned2['img1']
        request.user.first_name=cleaned1['first_name']
        request.user.last_name=cleaned1['last_name']
        request.user.email=cleaned1['email']
        if 'username' in cleaned1:
            request.user.username=cleaned1['username']
        request.user.person.occupation=cleaned2['occupation']
        request.user.person.skills=cleaned2['skills']
        request.user.person.hobbies=cleaned2['hobbies']
        if (cleaned2['desc']!=''): 
                request.user.person.desc=cleaned2['desc']
        if ('linkedin' in cleaned2):
            request.user.person.linkedin=cleaned2['linkedin']
        else:
            messages.error(request, "Invalid URL entered before")
        if ('github' in cleaned2):
            request.user.person.github=cleaned2['github']
        else:
            messages.error(request, "Invalid URL entered before")
        request.user.person.save()
        request.user.save()

        return redirect(reverse_lazy("pfapp:dashboard"))   



class Project(View):
    def post(self,request):
        pid=request.POST.get('projectID')

        #Deleting The project
        if (request.POST.get('btn--delete') and pid!="-1"):
            request.user.person.projects_set.get(pk=pid).delete()
            return redirect(reverse_lazy("pfapp:dashboard"))

        #Handling Data
        form3=DashboardFormProjects(request.POST)
        form3.is_valid()
        cleaned3=form3.cleaned_data
        # print("In project view")
        # print(cleaned3)

        #Old project
        if (pid!="new"):
            projid=request.user.person.projects_set.get(pk=pid)
            # print(projid)
            projid.project_name=cleaned3['project_name']
            if ('url' in cleaned3):
                projid.url=cleaned3['url']
            else:
                messages.error(request, "Invalid URL entered before")
            if (cleaned3['desc']!=''): 
                projid.desc=cleaned3['desc']
            projid.save()
        #New Project
        else:
            if ('url' not in cleaned3):
                messages.error(request, "Invalid URL entered before")
            else:
                request.user.person.projects_set.create(project_name=cleaned3['project_name'],url=cleaned3['url'],desc=cleaned3['desc'])    
        return redirect(reverse_lazy("pfapp:dashboard"))


class Work(View):
    def post(self,request):
        workid=request.POST.get('workID')

        #Deletion
        if (request.POST.get('btn--delete') and workid!="-1"):
            request.user.person.work_set.get(pk=workid).delete()
            return redirect(reverse_lazy("pfapp:dashboard"))
        

        #Handling Data
        form4=DashboardFormWork(request.POST)
        form4.is_valid()
        cleaned4=form4.cleaned_data

        #New work
        if (workid=="new"):
            print(cleaned4)
            request.user.person.work_set.create(role=cleaned4['role'],company=cleaned4['company'],desc=cleaned4['desc'])
        #Old Work
        else:
            # print(cleaned4)
            wid=request.user.person.work_set.get(pk=workid)
            # print(wid)
            wid.role=cleaned4['role']
            wid.company=cleaned4['company']
            if (cleaned4['desc']!=''): 
                wid.desc=cleaned4['desc']
            wid.save()

        return redirect(reverse_lazy("pfapp:dashboard"))



#LOGOUT PAGE 
def logout_view(request):
    logout(request)
    messages.success(request,"Logged out successfully.")
    return redirect(reverse_lazy('pfapp:Get_started'))


# PORTFOLIO VIEW
class Portfolio(View):                                 
    def get(self, request, num) :
        print("here",num)
        if (num=='1'):
            return render(request,'pfapp/portfolio1.html',{'user':request.user})
        elif (num=='X'):
            return redirect("pfapp:dashboard")
        # return render(request,'pfapp/portfolio1.html',{'user':request.user})

class PortfolioAPI(APIView):
    # serializer_class = ReactSerializer
    def get(self, request):
        output_list = [{
                    "first_name":output.user.first_name,
                    "last_name":output.user.last_name,
                    "username":output.user.username,
                    "email":output.user.email,
                    "skills": output.skills, 
                    "hobbies": output.hobbies, 
                    "occupation": output.occupation,
                    "github":output.github,
                    "linkedin":output.linkedin,
                    "aboutme":output.desc,
                    "projects":[
                        {
                            "name":x.project_name,
                            "url":x.url,
                            "desc":x.desc
                        }
                            for x in output.projects_set.all()
                    ],
                    "work_exp":[
                        {
                            "role":x.role,
                            "company":x.company,
                            "desc":x.desc
                        }
                            for x in output.work_set.all()
                    ]
                }
            for output in Person.objects.all()]
        return Response(output_list)

    # def post(self, request):

    #     serializer = ReactSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)

class APIViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.order_by('id')
    serializer_class = Personserializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


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
    



#DEPRECIATED

       #Deleting a work exp or project
        # pid=request.POST.get('projectID')
        # workid=request.POST.get('workID')
        # if (request.POST.get('btn--delete') and pid!="-1"):
        #     request.user.person.projects_set.get(pk=pid).delete()
        #     return redirect(request.path)
        # elif (request.POST.get('btn--delete') and workid!="-1"):
        #     request.user.person.work_set.get(pk=workid).delete()
        #     return redirect(request.path)
        #Forms and cleaning
        # form1=DashboardFormUser(request.POST)
        # form2=DashboardFormPersonal(request.POST)
        # form3=DashboardFormProjects(request.POST)
        # form4=DashboardFormWork(request.POST)
        # form1.is_valid()
        # form2.is_valid()
        # form3.is_valid()
        # form4.is_valid()
        # cleaned1=form1.cleaned_data
        # cleaned2=form2.cleaned_data
        # cleaned3=form3.cleaned_data
        # cleaned4=form4.cleaned_data

        #Handling Persons
        # if (pid=="-1" and workid=="-1"):
        #     print(cleaned1)
        #     request.user.first_name=cleaned1['first_name']
        #     request.user.last_name=cleaned1['last_name']
        #     request.user.email=cleaned1['email']
        #     if 'username' in cleaned1:
        #         request.user.username=cleaned1['username']
        #     request.user.person.occupation=cleaned2['occupation']
        #     request.user.person.skills=cleaned2['skills']
        #     request.user.person.save()
        #     request.user.save()

        #Handling New Projects
        # if (pid!="new" and workid=="-1"):
        #     print(cleaned3)
        #     projid=request.user.person.projects_set.get(pk=pid)
        #     print(projid)
        #     projid.project_name=cleaned3['project_name']
        #     if ('url' in cleaned3):
        #         projid.url=cleaned3['url']
        #     else:
        #         messages.error(request, "Invalid URL entered before")
        #     if (cleaned3['desc']!=''): 
        #         projid.desc=cleaned3['desc']
        #     projid.save()

        #Handling New Work
        # elif (pid=="-1" and workid!="new"):
        #     print(cleaned4)
        #     wid=request.user.person.work_set.get(pk=workid)
        #     print(wid)
        #     wid.role=cleaned4['role']
        #     wid.company=cleaned4['company']
        #     if (cleaned4['desc']!=''): 
        #         wid.desc=cleaned4['desc']
        #     wid.save()

        # #Handling Old Projects
        # elif(pid!="-1"):
        #     print(cleaned3)
        #     if ('url' not in cleaned3):
        #         messages.error(request, "Invalid URL entered before")
        #     else:
        #         request.user.person.projects_set.create(project_name=cleaned3['project_name'],url=cleaned3['url'],desc=cleaned3['desc'])
        #Handling Old Work
        # else:
        #     print(cleaned4)
        #     request.user.person.work_set.create(role=cleaned4['role'],company=cleaned4['company'],desc=cleaned4['desc'])
        # return redirect(request.path)

