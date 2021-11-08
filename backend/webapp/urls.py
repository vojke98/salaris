from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    #path("", views.CityList, name="cities"),
    path("testfoobar/<str:message>/", views.testfoobar, name='testfoobar'),
    path("get_user_workhours/<int:user_id>/", views.get_user_workhours, name='get_user_workhours')
]