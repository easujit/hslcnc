from django.test import TestCase
from django.core.cache import cache
from .models import PolicyRule
from .authorization import authorize, selector_match, get_authorized_fields
from .evaluator import eval_condition

class PolicyRuleTestCase(TestCase):
    def setUp(self):
        cache.clear()
        
        self.allow_policy = PolicyRule.objects.create(
            tenant_id='H001',
            version=1,
            resource_type='field',
            action='read',
            selector={'form': 'visit_opd', 'field': 'hba1c'},
            effect='allow',
            condition="'Doctor' in user.roles",
            status='published'
        )
        
        self.deny_policy = PolicyRule.objects.create(
            tenant_id='H001',
            version=2,
            resource_type='field',
            action='write',
            selector={'form': 'visit_opd', 'field': 'hiv_status'},
            effect='deny',
            condition="'Nurse' in user.roles",
            status='published'
        )

    def test_policy_rule_creation(self):
        """Test PolicyRule model creation"""
        self.assertEqual(self.allow_policy.tenant_id, 'H001')
        self.assertEqual(self.allow_policy.resource_type, 'field')
        self.assertEqual(self.allow_policy.effect, 'allow')

    def test_selector_match(self):
        """Test selector matching logic"""
        self.assertTrue(selector_match(
            {'form': 'visit_opd', 'field': 'hba1c'},
            {'form': 'visit_opd', 'field': 'hba1c'}
        ))
        
        self.assertFalse(selector_match(
            {'form': 'visit_opd', 'field': 'hba1c'},
            {'form': 'visit_opd', 'field': 'name'}
        ))

    def test_authorize_allow(self):
        """Test authorization with allow policy"""
        user = {
            'tenant_id': 'H001',
            'roles': ['Doctor'],
            'departments': ['Endocrinology']
        }
        
        result = authorize(
            user,
            'field',
            'read',
            {'form': 'visit_opd', 'field': 'hba1c'}
        )
        self.assertTrue(result)

    def test_authorize_deny_overrides(self):
        """Test that deny policies override allow policies"""
        user = {
            'tenant_id': 'H001',
            'roles': ['Nurse'],
            'departments': ['Endocrinology']
        }
        
        result = authorize(
            user,
            'field',
            'write',
            {'form': 'visit_opd', 'field': 'hiv_status'}
        )
        self.assertFalse(result)

    def test_condition_evaluation(self):
        """Test condition evaluation"""
        user = {
            'tenant_id': 'H001',
            'roles': ['Doctor', 'Nurse'],
            'departments': ['Endocrinology']
        }
        
        result = eval_condition("'Doctor' in user.roles", user)
        self.assertTrue(result)
        
        result = eval_condition("'Admin' in user.roles", user)
        self.assertFalse(result)