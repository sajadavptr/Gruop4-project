from django.contrib import admin
from django.urls import include, path
#from django.views.generic.base import TemplateView # new
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('mania/', include('mania.urls')),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    
    
    
]

admin.site.site_header = 'Volleyball Mania Administration'
admin.site.site_title = 'Volleyball Mania'
admin.site.index_title= 'Volleyball Mania Administration'