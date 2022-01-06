from django.http import response
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

from django.http import HttpRequest
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils import tree
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import *
from . serializers import *

import json


# Create your views here.
def testfoobar(request, message):
    return HttpResponse("Hello %s, you little bitch!" % message)



def get_user_workhours(request, user_id):
    
    u = User.objects.get(pk=user_id)  # Check if null ?

    if u == None:                     # NE RADI
        return Http404           

    workhours = WorkhourSerializer(Workhour.objects.all().filter(user=u), many=True).data

    response = {}
    response['workhours'] = workhours

    return HttpResponse(json.dumps(response),
                        content_type="application/json",
                        status=status.HTTP_200_OK)


# Treba model companies promijeniti da se moze traziti po user_id
def get_user_companies(request, user_id):
    u = User.objects.get(pk=user_id)


def get_users_from_company(request, company_id):
    c = Company.objects.get(pk=company_id)

    users = UserSerializer(User.objects.all().filter(company=c), many=True).data

    response = {}
    response['users'] = users

    return HttpResponse(json.dumps(response),
                        content_type="application/json",
                        status=status.HTTP_200_OK)


def get_user_data(request, user_email):
    u = User.objects.get(email=user_email)

    user_data = UserSerializer(u).data

    response = {}
    response['user'] = user_data

    return HttpResponse(json.dumps(response),
                        content_type="application/json",
                        status=status.HTTP_200_OK)
    

##########  CITY  ############
class CityList(APIView):

    def get(self, request):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CityDetails(APIView):

    def get_object(self, pk):
        try:
            return City.objects.get(pk=pk)
        except City.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        city = self.get_object(pk)
        serializer = CitySerializer(city)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        city = self.get_object(pk)
        serializer = CitySerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        city = self.get_object(pk)
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


##########  ADDRESS  #############
class AddressList(APIView):

    def get(self, request):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddressDetails(APIView):

    def get_object(self, pk):
        try:
            return Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        address = self.get_object(pk)
        serializer = AddressSerializer(address)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        address = self.get_object(pk)
        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        address = self.get_object(pk)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


##########  ROLE  #############
class RoleList(APIView):

    def get(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoleDetails(APIView):

    def get_object(self, pk):
        try:
            return Role.objects.get(pk=pk)
        except Role.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        role = self.get_object(pk)
        serializer = RoleSerializer(role)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        role = self.get_object(pk)
        serializer = RoleSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        role = self.get_object(pk)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


##########  USER  #############
class UserList(APIView):

    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetails(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


##########  COMPANY  #############
class CompanyList(APIView):

    def get(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetails(APIView):

    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        company = self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


##########  WORKHOUR  #############
class WorkhourList(APIView):

    def get(self, request):
        workhour = Workhour.objects.all()
        serializer = WorkhourSerializer(workhour, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WorkhourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkhourDetails(APIView):

    def get_object(self, pk):
        try:
            return Workhour.objects.get(pk=pk)
        except Workhour.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        workhour = self.get_object(pk)
        serializer = WorkhourSerializer(workhour)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = WorkhourSerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        workhour = self.get_object(pk)
        workhour.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


##########  JOIN_REQUEST  #############
class JoinRequestList(APIView):

    def get(self, request):
        joinRequest = JoinRequest.objects.all()
        serializer = JoinRequestSerializer(joinRequest, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JoinRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JoinRequestDetails(APIView):

    def get_object(self, pk):
        try:
            return JoinRequest.objects.get(pk=pk)
        except JoinRequest.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        joinRequest = self.get_object(pk)
        serializer = JoinRequestSerializer(joinRequest)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        joinRequest = self.get_object(pk)
        serializer = JoinRequestSerializer(joinRequest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        joinRequest = self.get_object(pk)
        joinRequest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)