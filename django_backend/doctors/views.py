from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework.permissions import IsAuthenticated

class DoctorListView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]