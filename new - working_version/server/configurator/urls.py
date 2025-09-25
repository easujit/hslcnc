from django.urls import path
from . import views

urlpatterns = [
    path('seed/', views.seed_config),
    path('effective/form/<str:name>/', views.effective_form),
    path('effective/rules/<str:name>/', views.effective_rules),
    path('effective/workflow/<str:name>/', views.effective_workflow),
    path('publish/<str:kind>/<str:name>/', views.publish_config),
]