from django.db import models

class Config(models.Model):
    KIND_CHOICES = [
        ('form', 'Form'),
        ('rule', 'Rule'),
        ('workflow', 'Workflow'),
    ]
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    kind = models.CharField(max_length=20, choices=KIND_CHOICES)
    name = models.CharField(max_length=100)
    version = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    scope = models.CharField(max_length=100, default='global')
    spec_json = models.JSONField(default=dict)

    class Meta:
        unique_together = ('kind', 'name', 'version', 'scope')

    def __str__(self):
        return f"{self.kind}:{self.name}:v{self.version} ({self.status})"