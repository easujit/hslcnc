"""
Consent Management URLs
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'consents', views.ConsentViewSet)
router.register(r'consent-requests', views.ConsentRequestViewSet)
router.register(r'audit-events', views.AuditEventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    # Consent checking
    path('consent/check/', views.check_consent, name='check_consent'),
    path('consent/<str:consent_id>/revoke/', views.revoke_consent, name='revoke_consent'),
    path('patients/<str:patient_id>/consents/', views.patient_consents, name='patient_consents'),
    
    # ABDM endpoints
    path('abdm/request-consent/', views.abdm_request_consent, name='abdm_request_consent'),
    path('abdm/notify/', views.abdm_notify, name='abdm_notify'),
    path('abdm/fetch-artefact/', views.abdm_fetch_artefact, name='abdm_fetch_artefact'),
]
