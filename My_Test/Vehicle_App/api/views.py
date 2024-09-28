from rest_framework import viewsets
from Vehicle_App.api.serializers import VehicleSerializer
from Vehicle_App.models import Vehicle

class VehicleCRUDCBV(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


