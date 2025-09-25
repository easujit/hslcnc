#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diabetes_poc.settings')
django.setup()

from runtime_engine.views import _safe_eval

# Test the specific expression that's failing
test_data = {"age": 12}

print("Testing individual expressions:")
try:
    result1 = _safe_eval("age is not None", test_data)
    print(f"age is not None: {result1}")
except Exception as e:
    print(f"age is not None ERROR: {e}")

try:
    result2 = _safe_eval("age < 18", test_data)
    print(f"age < 18: {result2}")
except Exception as e:
    print(f"age < 18 ERROR: {e}")

try:
    result3 = _safe_eval("(age is not None) and (age < 18)", test_data)
    print(f"(age is not None) and (age < 18): {result3}")
except Exception as e:
    print(f"(age is not None) and (age < 18) ERROR: {e}")

# Test with different data types
test_data_int = {"age": 12}
test_data_float = {"age": 12.0}
test_data_str = {"age": "12"}

print("\nTesting with different data types:")
for data_type, data in [("int", test_data_int), ("float", test_data_float), ("str", test_data_str)]:
    try:
        result = _safe_eval("(age is not None) and (age < 18)", data)
        print(f"{data_type}: {result}")
    except Exception as e:
        print(f"{data_type} ERROR: {e}")
