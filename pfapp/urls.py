from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views



app_name="pfapp"
urlpatterns = [
    path("",views.Get_started.as_view(),name="Get_started"),
    path("register/",views.Register.as_view(),name="register"),
    path("accounts/login/", views.UpdatedLoginView.as_view(extra_context={"leftclass":"d-none d-md-block"})),
    path("dashboard/",views.Dashboard.as_view(),name="dashboard"),
    path("portfolio_api/",views.PortfolioAPI.as_view(),name="portfolio"),
    path("logout/",views.logout_view,name="logout"),

]