
from django.db import models
class Config(models.Model):
    KIND_CHOICES=[("form","form"),("rule","rule"),("workflow","workflow")]
    kind=models.CharField(max_length=20, choices=KIND_CHOICES)
    name=models.CharField(max_length=100)
    scope=models.JSONField(default=dict)
    version=models.IntegerField(default=1)
    status=models.CharField(max_length=20, default="published")
    spec=models.JSONField(default=dict)
    class Meta: unique_together=("kind","name","version")
    def __str__(self): return f"{self.kind}:{self.name}:v{self.version} ({self.status})"
