from rest_framework import serializers
from .models import Driver

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'name', 'mobile_number', 'email', 'city', 'district', 'language', 'assigned_truck')
