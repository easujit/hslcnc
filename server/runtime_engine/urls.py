from django.urls import path
from . import views

urlpatterns = [
    path('rules/evaluate/<str:form>/', views.evaluate_rules),
]