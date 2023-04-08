from django.urls import path
from .views import DriverList, DriverDetail

urlpatterns = [
    path('driver/', DriverList.as_view(), name='driver-list'),
    path('driver/<int:pk>/', DriverDetail.as_view(), name='driver-detail'),
]
