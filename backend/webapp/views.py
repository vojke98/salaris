from django.contrib.auth.models import User, Group
from rest_framework import generics, viewsets, permissions, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import *

##########  CITY  ############
class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all().order_by("pk")
    #permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = City.objects.all()
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = City.objects.all()
        city = get_object_or_404(queryset, pk=pk)
        serializer = CitySerializer(city)
        return Response(serializer.data)

    def create(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


##########  ADDRESS  #############
class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    def list(self, request):
        queryset = Address.objects.all()
        serializer = AddressSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Address.objects.all()
        address = get_object_or_404(queryset, pk=pk)
        serializer = AddressSerializer(address)
        return Response(serializer.data)

    def create(self, request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


##########  ROLE  #############
class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

    def list(self, request):
        queryset = Role.objects.all()
        serializer = RoleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Role.objects.all()
        role = get_object_or_404(queryset, pk=pk)
        serializer = RoleSerializer(role)
        return Response(serializer.data)

    def create(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


##########  USER  #############
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request):
        queryset = self.queryset
        company = self.request.query_params.get('company')
        if company is not None: queryset = queryset.filter(company=company)
        email = self.request.query_params.get('email')
        if email is not None:  queryset = queryset.filter(email=email)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.queryset
        if pk is not None: user = get_object_or_404(queryset, pk=pk)
        else:
            email = self.request.query_params.get('email')
            password = self.request.query_params.get('password')
            user = get_object_or_404(queryset, email=email, password=password)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


##########  COMPANY  #############
class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def list(self, request):
        queryset = Company.objects.all()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Company.objects.all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def create(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


##########  WORKHOUR  #############
class WorkhourViewSet(viewsets.ModelViewSet):
    serializer_class = WorkhourSerializer
    queryset = Workhour.objects.all()

    def list(self, request):
        queryset = Workhour.objects.all()
        user = self.request.query_params.get('user')
        if user is not None:  queryset = queryset.filter(user=user)
        serializer = WorkhourSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Workhour.objects.all()
        workhour = get_object_or_404(queryset, pk=pk)
        serializer = WorkhourSerializer(workhour)
        return Response(serializer.data)

    def create(self, request):
        serializer = WorkhourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


##########  JOIN_REQUEST  #############
class JoinRequestViewSet(viewsets.ModelViewSet):
    serializer_class = JoinRequestSerializer
    queryset = JoinRequest.objects.all()

    def list(self, request):
        queryset = JoinRequest.objects.all()
        company = self.request.query_params.get('company')
        if company is not None: queryset = queryset.filter(company=company)
        serializer = JoinRequestSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = JoinRequest.objects.all()
        joinRequest = get_object_or_404(queryset, pk=pk)
        serializer = JoinRequestSerializer(joinRequest)
        return Response(serializer.data)

    def create(self, request):
        serializer = JoinRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)