from rest_framework import serializers
from configurator.models import Config
from clinical.models import Patient, Visit, Document
from submission.models import Submission
from orchestrator.models import Outbox, Notification, Task

class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = "__all__"

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

class VisitSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    patient_external_id = serializers.CharField(source='patient.external_id', read_only=True)
    
    class Meta:
        model = Visit
        fields = "__all__"

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = "__all__"

class OutboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outbox
        fields = "__all__"

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"