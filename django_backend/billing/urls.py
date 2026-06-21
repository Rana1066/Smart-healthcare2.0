from django.urls import path
from .views import BillingListView

urlpatterns = [
    path("", BillingListView.as_view()),
]