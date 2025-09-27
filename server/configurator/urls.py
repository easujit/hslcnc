from django.urls import path
from . import views

urlpatterns = [
    path('seed/', views.seed_config),
    path('effective/form/<str:name>/', views.effective_form),
    path('effective/rules/<str:name>/', views.effective_rules),
    path('effective/workflow/<str:name>/', views.effective_workflow),
    path('publish/<str:kind>/<str:name>/', views.publish_config),
    path('versions/<str:kind>/<str:name>/', views.get_versions),
    path('rollback/<str:kind>/<str:name>/', views.rollback_config),
    path('validate/<str:name>/', views.validate_form_data),
    path('templates/fields/', views.get_field_templates),
    path('templates/forms/', views.get_form_templates),
]