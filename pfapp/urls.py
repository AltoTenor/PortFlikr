from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views



app_name="pfapp"
urlpatterns = [
    path("",views.Get_started.as_view(),name="Get_started"),
    # path("register/",views.Reigster.as_view(),name=""),
    path("accounts/login/", auth_views.LoginView.as_view()),
    # path("dashboard/",views.Dashboard.as_view(),name="dashboard"),
    # path("portfolio/<first-name>",views.Portfolio.as_view(),name="portfolio"),
]