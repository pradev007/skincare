from django.shortcuts import render
from .serializers import ProgramSerializer
from .models import ProgramModel
from rest_framework import generics

# Create your views here.
class ProgramView(generics.ListCreateAPIView):
    queryset = ProgramModel.objects.all()
    serializer_class = ProgramSerializer