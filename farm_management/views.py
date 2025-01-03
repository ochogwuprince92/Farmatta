from rest_framework import generics
from .models import Crop, Land
from .serializers import CropSerializer, LandSerializer

class CropListCreateView(generics.ListCreateAPIView):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

class CropDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

class LandListCreateView(generics.ListCreateAPIView):
    queryset = Land.objects.all()
    serializer_class = LandSerializer

class LandDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Land.objects.all()
    serializer_class = LandSerializer