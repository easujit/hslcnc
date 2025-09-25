"""
Multi-tenancy models and managers
"""
from django.db import models
from django.core.exceptions import ValidationError
from .tenant import get_current_tenant, require_tenant

class TenantQuerySet(models.QuerySet):
    """
    QuerySet that automatically filters by tenant_id
    """
    
    def filter_by_tenant(self, tenant_id=None):
        """Filter queryset by tenant_id"""
        if tenant_id is None:
            tenant_id = get_current_tenant()
        
        if tenant_id:
            return self.filter(tenant_id=tenant_id)
        return self.none()
    
    def get_queryset(self):
        """Override to apply tenant filtering"""
        return self.filter_by_tenant()

class TenantManager(models.Manager):
    """
    Manager that automatically applies tenant filtering
    """
    
    def get_queryset(self):
        """Return queryset filtered by current tenant"""
        queryset = super().get_queryset()
        tenant_id = get_current_tenant()
        
        if tenant_id and hasattr(queryset.model, 'tenant_id'):
            return queryset.filter(tenant_id=tenant_id)
        
        return queryset
    
    def all(self):
        """Return all objects for current tenant"""
        return self.get_queryset()
    
    def create(self, **kwargs):
        """Create object with tenant_id if not provided"""
        if 'tenant_id' not in kwargs:
            kwargs['tenant_id'] = get_current_tenant()
        return super().create(**kwargs)

class AbstractTenantModel(models.Model):
    """
    Abstract base model for tenant-aware models
    """
    tenant_id = models.CharField(max_length=100, db_index=True, help_text="Tenant identifier")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
    
    def save(self, *args, **kwargs):
        """Auto-set tenant_id if not provided"""
        if not self.tenant_id:
            self.tenant_id = get_current_tenant()
        
        if not self.tenant_id:
            raise ValidationError("Tenant context required")
        
        super().save(*args, **kwargs)
    
    def clean(self):
        """Validate tenant_id is set"""
        if not self.tenant_id:
            raise ValidationError("Tenant ID is required")
        super().clean()
    
    @classmethod
    def get_tenant_objects(cls, tenant_id=None):
        """Get objects for specific tenant"""
        if tenant_id is None:
            tenant_id = get_current_tenant()
        return cls.objects.filter(tenant_id=tenant_id)
