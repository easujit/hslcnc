from django.urls import path
from .views import evaluate_rules
urlpatterns=[path('rules/evaluate/<str:form_name>/', evaluate_rules)]
