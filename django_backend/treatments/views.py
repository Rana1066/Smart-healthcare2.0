from rest_framework import generics
from .models import Treatment
from .serializers import TreatmentSerializer
from rest_framework.permissions import IsAuthenticated

class TreatmentListView(generics.ListAPIView):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
    permission_classes = [IsAuthenticated]