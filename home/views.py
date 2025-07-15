from django.shortcuts import render
from .serializers import HeadingSerializer
from .models import HeadingModel
from rest_framework import generics

# Create your views here.
class HeadingViews(generics.ListAPIView):
    queryset = HeadingModel.objects.all()
    serializer_class = HeadingSerializer
    