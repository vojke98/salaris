from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    #path("", views.CityList, name="cities"),
    path("testfoobar/<str:message>/", views.testfoobar, name='testfoobar'),
    path("get_user_workhours/<int:user_id>/", views.get_user_workhours, name='get_user_workhours'),

    path('cities/', views.CityList.as_view()),
    path('cities/<int:pk>/', views.CityDetails.as_view()),

    path('addresses/', views.AddressList.as_view()),
    path('addresses/<int:pk>/', views.AddressDetails.as_view()),

    path('roles/', views.RoleList.as_view()),
    path('roles/<int:pk>/', views.RoleDetails.as_view()),

    path('user/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetails.as_view()),

    path('companies/', views.CompanyList.as_view()),
    path('companies/<int:pk>/', views.CompanyDetails.as_view()),

    path('workhours/', views.WorkhourList.as_view()),
    path('workhours/<int:pk>/', views.WorkhourDetails.as_view()),

    path('join-request/', views.JoinRequestList.as_view()),
    path('join-request/<int:pk>/', views.JoinRequestDetails.as_view()),

    path('leave-request/', views.LeaveRequestList.as_view()),
    path('leave-request/<int:pk>/', views.LeaveRequestDetails.as_view()),
]