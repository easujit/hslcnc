from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import ExtensionFunction, ExtensionHook, ExtSubscription, DeadLetter
from .serializers import (
    ExtensionFunctionSerializer, 
    ExtensionHookSerializer, 
    ExtSubscriptionSerializer, 
    DeadLetterSerializer
)

@method_decorator(csrf_exempt, name='dispatch')
class ExtensionFunctionViewSet(viewsets.ModelViewSet):
    """CRUD operations for Extension Functions"""
    queryset = ExtensionFunction.objects.all()
    serializer_class = ExtensionFunctionSerializer
    permission_classes = [AllowAny]

    def list(self, request):
        """List all extension functions"""
        functions = ExtensionFunction.objects.all()
        serializer = self.get_serializer(functions, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create new extension function"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """Update extension function"""
        try:
            function = ExtensionFunction.objects.get(pk=pk)
        except ExtensionFunction.DoesNotExist:
            return Response({'error': 'Extension function not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(function, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Delete extension function"""
        try:
            function = ExtensionFunction.objects.get(pk=pk)
            function.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ExtensionFunction.DoesNotExist:
            return Response({'error': 'Extension function not found'}, status=status.HTTP_404_NOT_FOUND)

@method_decorator(csrf_exempt, name='dispatch')
class ExtensionHookViewSet(viewsets.ModelViewSet):
    """CRUD operations for Extension Hooks"""
    queryset = ExtensionHook.objects.all()
    serializer_class = ExtensionHookSerializer
    permission_classes = [AllowAny]

    def list(self, request):
        """List all extension hooks"""
        hooks = ExtensionHook.objects.all()
        serializer = self.get_serializer(hooks, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create new extension hook"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """Update extension hook"""
        try:
            hook = ExtensionHook.objects.get(pk=pk)
        except ExtensionHook.DoesNotExist:
            return Response({'error': 'Extension hook not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(hook, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Delete extension hook"""
        try:
            hook = ExtensionHook.objects.get(pk=pk)
            hook.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ExtensionHook.DoesNotExist:
            return Response({'error': 'Extension hook not found'}, status=status.HTTP_404_NOT_FOUND)

@method_decorator(csrf_exempt, name='dispatch')
class ExtSubscriptionViewSet(viewsets.ModelViewSet):
    """CRUD operations for Event Subscriptions"""
    queryset = ExtSubscription.objects.all()
    serializer_class = ExtSubscriptionSerializer
    permission_classes = [AllowAny]

    def list(self, request):
        """List all subscriptions"""
        subscriptions = ExtSubscription.objects.all()
        serializer = self.get_serializer(subscriptions, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create new subscription"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """Update subscription"""
        try:
            subscription = ExtSubscription.objects.get(pk=pk)
        except ExtSubscription.DoesNotExist:
            return Response({'error': 'Subscription not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(subscription, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Delete subscription"""
        try:
            subscription = ExtSubscription.objects.get(pk=pk)
            subscription.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ExtSubscription.DoesNotExist:
            return Response({'error': 'Subscription not found'}, status=status.HTTP_404_NOT_FOUND)

class DeadLetterViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only operations for Dead Letter Queue"""
    queryset = DeadLetter.objects.all()
    serializer_class = DeadLetterSerializer
    permission_classes = [AllowAny]

    def list(self, request):
        """List all dead letters"""
        dead_letters = DeadLetter.objects.all()
        serializer = self.get_serializer(dead_letters, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def retry(self, request, pk=None):
        """Retry a dead letter message"""
        try:
            dead_letter = DeadLetter.objects.get(pk=pk)
            # This would trigger a retry mechanism
            # For now, just increment retry count
            dead_letter.retry_count += 1
            dead_letter.save()
            return Response({'message': 'Retry initiated'})
        except DeadLetter.DoesNotExist:
            return Response({'error': 'Dead letter not found'}, status=status.HTTP_404_NOT_FOUND)