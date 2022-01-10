from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    #path("", views.CityList, name="cities"),
    path("testfoobar/<str:message>/", views.testfoobar, name='testfoobar'),
    path("get-user-workhours/<int:user_id>/", views.get_user_workhours, name='get_user_workhours'),
    path("get-users-from-company/<int:company_id>/", views.get_users_from_company, name='get_users_from_company'),
    path("get-user-data/<str:user_email>/", views.get_user_data, name='get_user_data'),
    path("create-user/", views.create_user, name='create_user'),
    path("create-workhour/", views.create_workhour, name='create_workhour'),
    path("create-company/", views.create_company, name='create_company'),
    path("create-join-request/", views.create_join_request, name='create_join_request'),

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
]