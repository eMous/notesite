from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TodoSerializer
from .models.site_application import *

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = InstantContent.objects.all()

# Create your views here.
