from rest_framework import generics
from .models import Billing
from .serializers import BillingSerializer
from rest_framework.permissions import IsAuthenticated

class BillingListView(generics.ListAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
    permission_classes = [IsAuthenticated]