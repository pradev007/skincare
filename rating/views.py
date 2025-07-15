from django.shortcuts import render
from .models import RatingModel
from .serializers import RatingSerialzier
from rest_framework import generics

# Create your views here.
class RatingView(generics.ListAPIView):
    queryset = RatingModel.objects.all()
    serializer_class = RatingSerialzier
