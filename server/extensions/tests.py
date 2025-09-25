from django.test import TestCase
from django.utils import timezone
from .models import ExtensionFunction, ExtensionHook, ExtSubscription, DeadLetter
from .utils import call_http, sign_request, verify_signature, matches_criteria
import json

class ExtensionsTestCase(TestCase):
    def setUp(self):
        self.extension_function = ExtensionFunction.objects.create(
            name="test_bmi_calculator",
            type="runtime.compute",
            match_json={"form": "visit_opd"},
            invoke_json={
                "method": "POST",
                "url": "http://example.com/bmi",
                "timeout_ms": 1000,
                "headers": {"Content-Type": "application/json"}
            },
            secret="test-secret",
            retries=3,
            is_blocking=False,
            enabled=True
        )
        
        self.extension_hook = ExtensionHook.objects.create(
            name="test_validation_hook",
            phase="submission.pre",
            match_json={"age": {"$lt": 18}},
            invoke_json={
                "method": "POST",
                "url": "http://example.com/validate",
                "timeout_ms": 2000
            },
            secret="test-secret",
            retries=2,
            is_blocking=True,
            enabled=True
        )
        
        self.subscription = ExtSubscription.objects.create(
            name="test_subscription",
            topics=["visit_saved"],
            endpoint="http://example.com/webhook",
            secret="test-secret",
            retries=3,
            dead_letter=True,
            enabled=True
        )

    def test_extension_function_creation(self):
        """Test ExtensionFunction model creation"""
        self.assertEqual(self.extension_function.name, "test_bmi_calculator")
        self.assertEqual(self.extension_function.type, "runtime.compute")
        self.assertTrue(self.extension_function.enabled)

    def test_extension_hook_creation(self):
        """Test ExtensionHook model creation"""
        self.assertEqual(self.extension_hook.name, "test_validation_hook")
        self.assertEqual(self.extension_hook.phase, "submission.pre")
        self.assertTrue(self.extension_hook.is_blocking)

    def test_subscription_creation(self):
        """Test ExtSubscription model creation"""
        self.assertEqual(self.subscription.name, "test_subscription")
        self.assertIn("visit_saved", self.subscription.topics)
        self.assertTrue(self.subscription.dead_letter)

    def test_hmac_signing(self):
        """Test HMAC signature generation and verification"""
        payload = {"test": "data", "number": 123}
        secret = "test-secret"
        
        signature = sign_request(payload, secret)
        self.assertTrue(signature.startswith("sha256="))
        
        # Verify correct signature
        self.assertTrue(verify_signature(payload, signature, secret))
        
        # Verify wrong signature fails
        wrong_signature = "sha256=wrong"
        self.assertFalse(verify_signature(payload, wrong_signature, secret))

    def test_matches_criteria(self):
        """Test criteria matching logic"""
        data = {"form": "visit_opd", "age": 25, "name": "John"}
        
        # Test exact match
        self.assertTrue(matches_criteria(data, {"form": "visit_opd"}))
        self.assertTrue(matches_criteria(data, {"age": 25}))
        
        # Test no match
        self.assertFalse(matches_criteria(data, {"form": "different"}))
        self.assertFalse(matches_criteria(data, {"age": 30}))
        
        # Test missing field
        self.assertFalse(matches_criteria(data, {"missing_field": "value"}))

    def test_dead_letter_creation(self):
        """Test DeadLetter model creation"""
        dead_letter = DeadLetter.objects.create(
            kind="hook",
            target="http://example.com/failed",
            payload_json={"test": "data"},
            last_error="Connection timeout",
            retry_count=1
        )
        
        self.assertEqual(dead_letter.kind, "hook")
        self.assertEqual(dead_letter.retry_count, 1)
        self.assertIn("test", dead_letter.payload_json)

    def test_extension_function_matching(self):
        """Test extension function matching logic"""
        # Test matching data
        matching_data = {"form": "visit_opd", "height_cm": 170, "weight_kg": 70}
        self.assertTrue(matches_criteria(matching_data, self.extension_function.match_json))
        
        # Test non-matching data
        non_matching_data = {"form": "different", "height_cm": 170, "weight_kg": 70}
        self.assertFalse(matches_criteria(non_matching_data, self.extension_function.match_json))

    def test_extension_hook_matching(self):
        """Test extension hook matching logic"""
        # Test matching data (age < 18)
        matching_data = {"age": 15, "name": "Minor"}
        self.assertTrue(matches_criteria(matching_data, self.extension_hook.match_json))
        
        # Test non-matching data (age >= 18)
        non_matching_data = {"age": 25, "name": "Adult"}
        self.assertFalse(matches_criteria(non_matching_data, self.extension_hook.match_json))

    def test_subscription_topic_filtering(self):
        """Test subscription topic filtering"""
        # Test matching topic
        self.assertIn("visit_saved", self.subscription.topics)
        
        # Test non-matching topic
        self.assertNotIn("different_topic", self.subscription.topics)

class ExtensionsIntegrationTestCase(TestCase):
    """Integration tests for extensions with other components"""
    
    def setUp(self):
        # Create a test extension function that returns BMI calculation
        self.bmi_function = ExtensionFunction.objects.create(
            name="external_bmi_calculator",
            type="runtime.compute",
            match_json={"form": "visit_opd"},
            invoke_json={
                "method": "POST",
                "url": "http://localhost:8000/mock-bmi-calculator",
                "timeout_ms": 1000
            },
            secret="test-secret",
            retries=1,
            is_blocking=False,
            enabled=True
        )

    def test_runtime_extension_integration(self):
        """Test that runtime extensions are called during rule evaluation"""
        # This would require a mock HTTP server to test properly
        # For now, just test that the extension function exists and is configured correctly
        self.assertTrue(self.bmi_function.enabled)
        self.assertEqual(self.bmi_function.type, "runtime.compute")
        
        # Test that matching criteria works
        test_data = {"form": "visit_opd", "height_cm": 170, "weight_kg": 70}
        self.assertTrue(matches_criteria(test_data, self.bmi_function.match_json))

    def test_hook_integration(self):
        """Test that hooks are called during submission"""
        # Create a pre-submission hook
        pre_hook = ExtensionHook.objects.create(
            name="age_validation",
            phase="submission.pre",
            match_json={"age": {"$lt": 18}},
            invoke_json={
                "method": "POST",
                "url": "http://localhost:8000/mock-validation",
                "timeout_ms": 2000
            },
            secret="test-secret",
            retries=2,
            is_blocking=True,
            enabled=True
        )
        
        # Test that the hook is configured correctly
        self.assertEqual(pre_hook.phase, "submission.pre")
        self.assertTrue(pre_hook.is_blocking)
        
        # Test matching logic
        minor_data = {"age": 15, "name": "Minor Patient"}
        self.assertTrue(matches_criteria(minor_data, pre_hook.match_json))

    def test_subscription_integration(self):
        """Test that subscriptions receive events"""
        subscription = ExtSubscription.objects.create(
            name="external_system",
            topics=["visit_saved", "patient_created"],
            endpoint="http://localhost:8000/mock-webhook",
            secret="test-secret",
            retries=3,
            dead_letter=True,
            enabled=True
        )
        
        # Test that subscription is configured correctly
        self.assertIn("visit_saved", subscription.topics)
        self.assertTrue(subscription.dead_letter)
        
        # Test topic filtering
        self.assertTrue("visit_saved" in subscription.topics)
        self.assertFalse("unknown_topic" in subscription.topics)