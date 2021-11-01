from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path("", views.CityList, name="cities"),
    path("details/<int:pk>/", views.CityDetails, name="details"),
    path("create", views.CityCreate, name="create"),
    path("update/<int:pk>/", views.CityUpdate, name="update"),
    path("delete/<int:pk>/", views.CityDelete, name="delete"),
]