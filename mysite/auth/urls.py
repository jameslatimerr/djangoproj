from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from django.urls import path, include
from . import views
urlpatterns = [
    #path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('change-password/', auth_views.PasswordChangeView.as_view())
   

]
