from rest_framework import serializers
from .models import ExtensionFunction, ExtensionHook, ExtSubscription, DeadLetter

class ExtensionFunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtensionFunction
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class ExtensionHookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtensionHook
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class ExtSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtSubscription
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class DeadLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeadLetter
        fields = '__all__'
        read_only_fields = ['created_at', 'last_attempt']
