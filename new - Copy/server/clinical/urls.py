from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.patients_list),
    path('visits/', views.visits_list),
]