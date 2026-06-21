from rest_framework import generics
from .models import Appointment
from .serializers import AppointmentSerializer
from rest_framework.permissions import IsAuthenticated


class AppointmentListView(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]