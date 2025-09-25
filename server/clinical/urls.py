from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.patients_list),
    path('visits/', views.visits_list),
    path('visits/<int:visit_id>/', views.update_visit_data),
    path('visits/<int:visit_id>/update-status/', views.update_visit_status),
    path('visits/<int:visit_id>/complete/', views.complete_draft_visit),
    path('documents/upload/', views.upload_document),
    path('patients/<int:patient_id>/documents/', views.patient_documents),
]