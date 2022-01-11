from django.contrib.auth.models import User, Group
from rest_framework import generics, viewsets, permissions, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import *
import json

##########  CITY  ############
class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all().order_by("pk")
    #permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.queryset
        city = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(city)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


##########  ADDRESS  #############
class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.queryset
        address = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(address)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


##########  ROLE  #############
class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.queryset
        role = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(role)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
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
        body = request.body.decode("utf-8").strip()
        content = json.loads(body or "null") # GET REQUEST BODY AND PARSE IT TO JSON
        if content is not None:
            if "company" in content:  queryset = queryset.filter(company=content["company"]) # CHECK IF KEY EXISTS, IF TRUE FILTER BY VALUE
            if "email" in content: queryset = queryset.filter(email=content["email"]) # CHECK IF KEY EXISTS, IF TRUE FILTER BY VALUE

        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.queryset
        user = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
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
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.queryset
        company = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(company)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


##########  WORKHOUR  #############
class WorkhourViewSet(viewsets.ModelViewSet):
    serializer_class = WorkhourSerializer
    queryset = Workhour.objects.all()

    def list(self, request):
        queryset = self.queryset
        body = request.body.decode("utf-8").strip()
        content = json.loads(body or "null") # GET REQUEST BODY AND PARSE IT TO JSON
        if content is not None:
            if "user" in content:  queryset = queryset.filter(company=content["user"]) # CHECK IF KEY EXISTS, IF TRUE FILTER BY VALUE

        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.queryset
        workhour = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(workhour)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


##########  JOIN_REQUEST  #############
class JoinRequestViewSet(viewsets.ModelViewSet):
    serializer_class = JoinRequestSerializer
    queryset = JoinRequest.objects.all()

    def list(self, request):
        queryset = self.queryset
        body = request.body.decode("utf-8").strip()
        content = json.loads(body or "null") # GET REQUEST BODY AND PARSE IT TO JSON
        if content is not None:
            if "company" in content:  queryset = queryset.filter(company=content["company"]) # CHECK IF KEY EXISTS, IF TRUE FILTER BY VALUE

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.queryset
        joinRequest = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(joinRequest)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)