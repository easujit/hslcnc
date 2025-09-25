from django.urls import path
from . import views

urlpatterns = [
    path('forms/visit_opd/submit/', views.submit_visit_opd),
]