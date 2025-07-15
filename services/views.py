from django.shortcuts import render
from .models import Services
from .serializers import ServicesSerialzier
from rest_framework import generics

# Create your views here.
class ServicesView(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerialzier