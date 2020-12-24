from django.shortcuts import render
from rest_framework import viewsets

from .serializers import UserSerializer
from .models.site_application import *


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = RecordedUser.objects.all()

# Create your views here.
