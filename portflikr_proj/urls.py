from django.contrib import admin
from django.contrib.auth import urls 
from django.urls import path,include
from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static


urlpatterns = [
    path("",include("pfapp.urls")),
    path('admin/', admin.site.urls),
    path("accounts/",include(urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)