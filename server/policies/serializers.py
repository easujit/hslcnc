from rest_framework import serializers
from django.db import models
from .models import PolicyRule

class PolicyRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyRule
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class PolicyRuleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyRule
        fields = ['tenant_id', 'resource_type', 'action', 'selector', 'effect', 'condition']
    
    def create(self, validated_data):
        # Auto-increment version for the tenant (across all statuses)
        tenant_id = validated_data['tenant_id']
        latest_version = PolicyRule.objects.filter(
            tenant_id=tenant_id
        ).aggregate(models.Max('version'))['version__max'] or 0
        validated_data['version'] = latest_version + 1
        return super().create(validated_data)

class PolicyRulePublishSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        # Publish the rule
        instance.status = 'published'
        instance.save()
        return instance
