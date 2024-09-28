from django.urls import path, include
from Vehicle_App import views
from rest_framework import routers
from Vehicle_App.api.views import VehicleCRUDCBV
router = routers.DefaultRouter()
router.register('vehicles_info', VehicleCRUDCBV)

urlpatterns = [
    path('', include(router.urls)),
]
