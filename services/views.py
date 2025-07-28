from django.shortcuts import render
from .models import Services
from .serializers import ServicesSerialzier
from rest_framework import generics ,permissions

# Create your views here.
class ServicesListCreateView(generics.ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerialzier
    # permission_classes = [permissions.IsAuthenticated]