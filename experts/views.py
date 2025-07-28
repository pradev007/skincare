from django.shortcuts import render
from .serializers import ExpertSerializer
from .models import ExpertModel
from rest_framework import generics , permissions


class ExpertListCreateApi(generics.ListCreateAPIView):
    queryset = ExpertModel.objects.all()
    serializer_class = ExpertSerializer
    permission_classes = [permissions.IsAuthenticated]

class ExpertRetrieveUpdateDeleteApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExpertModel.objects.all()
    serializer_class = ExpertSerializer
    permission_classes = [permissions.IsAuthenticated]