from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern
from rest_framework import routers
from webapp import views

router = routers.DefaultRouter()
router.register(r'cities', views.CityViewSet)
router.register(r'addresses', views.AddressViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'companies', views.CompanyViewSet)
router.register(r'workhours', views.WorkhourViewSet)
router.register(r'join-requests', views.JoinRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]