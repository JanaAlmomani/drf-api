from django.shortcuts import render
from rest_framework import generics
from .models import Snack 
from .serializers import SnackSerializer

# Create your views here.

# ListAPIView
class SnacksList(generics.ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer

# RetrieveAPIView RetrieveUpdateAPIView
class SnackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer