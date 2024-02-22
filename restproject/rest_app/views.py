from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .serializers import Userserializer
from .models import User


class Userviewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer
    
class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer

'''
ListCreateAPIView: Handles listing and creation of objects.
RetrieveUpdateDestroyAPIView: Handles retrieving, updating, and deleting a single object.
CreateAPIView: Handles creating objects.
ListAPIView: Handles listing objects.
RetrieveAPIView: Handles retrieving a single object.
UpdateAPIView: Handles updating a single object.
DestroyAPIView: Handles deleting a single object.

'''