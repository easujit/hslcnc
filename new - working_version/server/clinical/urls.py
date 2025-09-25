from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.patients_list),
    path('visits/', views.visits_list),
    path('documents/upload/', views.upload_document),
    path('patients/<int:patient_id>/documents/', views.patient_documents),
]