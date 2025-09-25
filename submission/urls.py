from django.urls import path
from .views import submit_visit_opd
urlpatterns=[path('forms/visit_opd/submit/', submit_visit_opd)]
