"""salaris URL Configuration

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
from rest_framework.urlpatterns import format_suffix_patterns
import webapp
from webapp import views
from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cities/', views.CityList.as_view()),
    path('api/cities/<int:pk>/', views.CityDetails.as_view()),

    path('api/addresses/', views.AddressList.as_view()),
    path('api/addresses/<int:pk>/', views.AddressDetails.as_view()),

    path('api/roles/', views.RoleList.as_view()),
    path('api/roles/<int:pk>/', views.RoleDetails.as_view()),

    path('api/staff/', views.StaffList.as_view()),
    path('api/staff/<int:pk>/', views.StaffDetails.as_view()),

    path('api/companies/', views.CompanyList.as_view()),
    path('api/companies/<int:pk>/', views.CompanyDetails.as_view()),

    path('api/workhours/', views.WorkhourList.as_view()),
    path('api/workhours/<int:pk>/', views.WorkhourDetails.as_view()),

    path('webapp/', include('webapp.urls'))
]
