"""
Consent Management Serializers
"""
from rest_framework import serializers
from .models import Consent, ConsentRequest, AuditEvent

class ConsentSerializer(serializers.ModelSerializer):
    """Serializer for Consent model"""
    
    class Meta:
        model = Consent
        fields = '__all__'
        read_only_fields = ['consent_id', 'created_at', 'updated_at']
    
    def validate_data_categories(self, value):
        """Validate data categories are valid"""
        valid_categories = [
            'demographics', 'vitals', 'labs', 'diagnosis', 'medications',
            'procedures', 'allergies', 'family_history', 'social_history',
            'insurance', 'billing', 'images', 'documents'
        ]
        
        for category in value:
            if category not in valid_categories:
                raise serializers.ValidationError(f"Invalid data category: {category}")
        
        return value
    
    def validate(self, data):
        """Validate consent data"""
        if data['date_range_start'] >= data['date_range_end']:
            raise serializers.ValidationError("Start date must be before end date")
        
        if data['date_range_end'] >= data['expiry']:
            raise serializers.ValidationError("End date must be before expiry")
        
        return data

class ConsentRequestSerializer(serializers.ModelSerializer):
    """Serializer for ConsentRequest model"""
    
    class Meta:
        model = ConsentRequest
        fields = '__all__'
        read_only_fields = ['request_id', 'created_at', 'updated_at']

class AuditEventSerializer(serializers.ModelSerializer):
    """Serializer for AuditEvent model (read-only)"""
    
    class Meta:
        model = AuditEvent
        fields = '__all__'
        read_only_fields = '__all__'

class ConsentCheckSerializer(serializers.Serializer):
    """Serializer for consent checking requests"""
    patient_id = serializers.CharField(max_length=100)
    purpose = serializers.ChoiceField(choices=Consent.PURPOSE_CHOICES)
    data_categories = serializers.ListField(
        child=serializers.CharField(max_length=50),
        allow_empty=False
    )
    action = serializers.ChoiceField(choices=AuditEvent.ACTION_CHOICES, default='read')
    resource = serializers.CharField(max_length=200, required=False)
    fields = serializers.ListField(
        child=serializers.CharField(max_length=100),
        required=False,
        default=list
    )

class ConsentCheckResponseSerializer(serializers.Serializer):
    """Serializer for consent checking responses"""
    allow = serializers.BooleanField()
    consent_id = serializers.CharField(max_length=100, allow_null=True)
    reason = serializers.CharField(max_length=500, allow_null=True)
    required_consent = serializers.DictField(allow_null=True)

class ConsentCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating new consents"""
    
    class Meta:
        model = Consent
        fields = [
            'patient_id', 'purpose', 'data_categories', 'date_range_start',
            'date_range_end', 'expiry', 'notice_lang', 'withdraw_url',
            'consent_method', 'consent_version', 'legal_basis'
        ]
    
    def create(self, validated_data):
        """Create consent with generated consent_id"""
        import uuid
        validated_data['consent_id'] = f"CONSENT_{uuid.uuid4().hex[:16].upper()}"
        return super().create(validated_data)

class ConsentRevokeSerializer(serializers.Serializer):
    """Serializer for revoking consents"""
    reason = serializers.CharField(max_length=500, required=False)
    revoked_by = serializers.CharField(max_length=100, required=False)
