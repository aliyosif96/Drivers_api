from django.db import models

# Create your models here.
from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    assigned_truck = models.ForeignKey('Truck', on_delete=models.SET_NULL, null=True)

class Truck(models.Model):
    number_plate = models.CharField(max_length=20, unique=True)
    registration_number = models.CharField(max_length=50, unique=True)
