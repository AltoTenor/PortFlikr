from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views



app_name="pfapp"
urlpatterns = [
    path("",views.Get_started.as_view(),name="Get_started"),
    path("register/",views.Register.as_view(),name="register"),
    path("accounts/login/", views.UpdatedLoginView.as_view(extra_context={"leftclass":"d-none d-md-block"})),
    path("dashboard/",views.Dashboard.as_view(),name="dashboard"),
    path("submit_profile/",views.Profile.as_view(),name="submit_profile"),
    path("submit_project/",views.Project.as_view(),name="submit_project"),
    path("submit_work/",views.Work.as_view(),name="submit_work"),
    path("portfolio_api/",views.PortfolioAPI.as_view(),name="portfolio"),
    path("portfolio_api_with_img/",views.APIViewSet.as_view({'get': 'list'}),name="api"),
    path("logout/",views.logout_view,name="logout"),

]