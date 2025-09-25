from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ExtensionFunctionViewSet, 
    ExtensionHookViewSet, 
    ExtSubscriptionViewSet, 
    DeadLetterViewSet
)

router = DefaultRouter()
router.register(r'functions', ExtensionFunctionViewSet, basename='extension-function')
router.register(r'hooks', ExtensionHookViewSet, basename='extension-hook')
router.register(r'subscriptions', ExtSubscriptionViewSet, basename='ext-subscription')
router.register(r'dead-letters', DeadLetterViewSet, basename='dead-letter')

urlpatterns = [
    path('', include(router.urls)),
]
