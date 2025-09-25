
from django.urls import path
from .views import list_visits, list_patients
urlpatterns = [
    path('visits/', list_visits),
    path('patients/', list_patients),
]
