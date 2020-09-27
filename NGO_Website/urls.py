"""NGO_Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from NGO_App.views import *
from django.conf import settings
from django.conf.urls.static import static
from NGO_App import api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('ngo_signup/',ngo_signup,name='ngo_signup'),
    path('user_signup/',user_signup,name='user_signup'),
    path('ngo_login/',ngo_login,name='ngo_login'),
    path('user_login/',user_login,name='user_login'),
    path('adminlogin/',adminlogin,name="adminlogin"),
    path('ngo_profile/',ngo_profile,name='ngo_profile'),
    path('user_profile/',user_profile,name='user_profile'),
    path('adminhome/',adminhome,name="adminhome"),
    path('logout/',Logout,name="logout"),
    path('all_verified_ngos/',all_verified_ngos,name='all_verified_ngos'),
    path('all_nonverified_ngos/',all_nonverified_ngos,name='all_nonverified_ngos'),
    path('verify_ngo/<int:pid>/',verify_ngo,name="verify_ngo"),
    path('delete_ngo/<int:pid>/',delete_ngo,name="delete_ngo"),
    path('view_users',view_users,name="view_users"),
    path('delete_ngo_2/<int:pid>/',delete_ngo_2,name="delete_ngo_2"),
    path('changepassworduser/',changepassworduser,name="changepassworduser"),
    path('changepasswordngo/',changepasswordngo,name="changepasswordngo"),
    path('ngo_add_requirements/',ngo_add_requirements,name="ngo_add_requirements"),
    path('user_ngo_view/',user_ngo_view,name="user_ngo_view"),
    path('user_ngo_information/<int:ngo_pk>/',user_ngo_information,name="user_ngo_information"),
    path('user_donator_list/',user_donator_list,name="user_donator_list"),
    path('ngo_self_requirements/',ngo_self_requirements,name="ngo_self_requirements"),
    path('api_user_profile/',api_views.UserProfileView.as_view()),
    path('api_ngo_profile/',api_views.NgoProfileView.as_view()),
    path('api_ngo_rquirement/',api_views.NgoRequirementsView.as_view()),
    path('api_reciept/',api_views.RecieptView.as_view()),
    path("api_ngo_login/",api_views.NgoLogin.as_view()),
    path("api_user_login/",api_views.UserLogin.as_view()),


]

if settings.DEBUG:
    urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
