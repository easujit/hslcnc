
from rest_framework import serializers
class VisitOpdSubmitSerializer(serializers.Serializer):
    patient_id = serializers.CharField()
    values = serializers.DictField()
