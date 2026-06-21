
from .models import Patient
from .serializers import PatientSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class PatientListView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]