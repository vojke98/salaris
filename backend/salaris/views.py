from django.shortcuts import render

from django.http import HttpRequest
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



def home(request):
    return render(request, 'webapp/home.html', { 'welcome' : "Hello there, welcome!"})