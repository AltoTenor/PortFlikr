from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.forms import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout
from django.urls import reverse_lazy
from .models import Person,Projects,Work




class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("first_name","last_name","username", "email", "password1", "password2")
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
                
        self.helper.form_show_labels=True
        self.helper.form_method = 'post'
        self.helper.form_action = reverse_lazy('projURLS:index')
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
                "username",
                'email',
                "password1", "password2",
        )
        self.helper.add_input(Submit('submit', 'Register'))



# class DashboardForm(forms.Form):
#     occupation = forms.CharField(label="Occupation",max_length=30,required=False)
#     project_name = forms.CharField(label="Project name",max_length=30,required=False)
#     url = forms.URLField(label="URL for the project",required=False)
#     desc = forms.CharField(label="Description",required=False)


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False)


class DashboardFormUser(ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","username", "email"]

class DashboardFormPersonal(ModelForm):
    class Meta:
        model = Person
        fields=['occupation','skills']


class DashboardFormProjects(ModelForm):
    class Meta:
        model = Projects
        exclude=['person']

class DashboardFormWork(ModelForm):
    class Meta:
        model = Work
        exclude=['start_date','end_date','person']