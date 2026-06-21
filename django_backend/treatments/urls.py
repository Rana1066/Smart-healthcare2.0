from django.urls import path
from .views import TreatmentListView

urlpatterns = [
    path("", TreatmentListView.as_view()),
]