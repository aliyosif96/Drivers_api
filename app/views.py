from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import filters
from .models import Driver
from .serializers import DriverSerializer

class DriverList(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['email', 'mobile_number', 'language', 'assigned_truck__number_plate']

class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
