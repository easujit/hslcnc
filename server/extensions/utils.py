import requests
import json
import hmac
import hashlib
import time
from typing import Tuple, Dict, Any, Optional
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def call_http(url: str, method: str = 'POST', json_data: Dict[str, Any] = None, 
              timeout_ms: int = 5000, headers: Dict[str, str] = None, 
              retries: int = 3) -> Tuple[bool, int, Dict[str, Any], Optional[str]]:
    """
    Make HTTP call with retries and error handling
    
    Returns:
        (success, status_code, response_json, error_message)
    """
    if json_data is None:
        json_data = {}
    if headers is None:
        headers = {}
    
    # Set default headers
    headers.setdefault('Content-Type', 'application/json')
    headers.setdefault('User-Agent', 'Hospital-POC-Extensions/1.0')
    
    timeout_seconds = timeout_ms / 1000.0
    
    for attempt in range(retries + 1):
        try:
            response = requests.request(
                method=method,
                url=url,
                json=json_data,
                headers=headers,
                timeout=timeout_seconds
            )
            
            # Try to parse JSON response
            try:
                response_json = response.json()
            except (ValueError, json.JSONDecodeError):
                response_json = {'raw_response': response.text}
            
            return True, response.status_code, response_json, None
            
        except requests.exceptions.Timeout:
            error_msg = f"Timeout after {timeout_seconds}s (attempt {attempt + 1}/{retries + 1})"
            logger.warning(f"HTTP call timeout: {url} - {error_msg}")
            if attempt == retries:
                return False, 0, {}, error_msg
                
        except requests.exceptions.ConnectionError as e:
            error_msg = f"Connection error (attempt {attempt + 1}/{retries + 1}): {str(e)}"
            logger.warning(f"HTTP connection error: {url} - {error_msg}")
            if attempt == retries:
                return False, 0, {}, error_msg
                
        except requests.exceptions.RequestException as e:
            error_msg = f"Request error (attempt {attempt + 1}/{retries + 1}): {str(e)}"
            logger.warning(f"HTTP request error: {url} - {error_msg}")
            if attempt == retries:
                return False, 0, {}, error_msg
                
        except Exception as e:
            error_msg = f"Unexpected error (attempt {attempt + 1}/{retries + 1}): {str(e)}"
            logger.error(f"HTTP unexpected error: {url} - {error_msg}")
            if attempt == retries:
                return False, 0, {}, error_msg
        
        # Wait before retry (exponential backoff)
        if attempt < retries:
            wait_time = min(2 ** attempt, 10)  # Max 10 seconds
            time.sleep(wait_time)
    
    return False, 0, {}, "Max retries exceeded"

def sign_request(payload: Dict[str, Any], secret: str) -> str:
    """Generate HMAC signature for request"""
    payload_str = json.dumps(payload, sort_keys=True, separators=(',', ':'))
    signature = hmac.new(
        secret.encode('utf-8'),
        payload_str.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    return f"sha256={signature}"

def verify_signature(payload: Dict[str, Any], signature: str, secret: str) -> bool:
    """Verify HMAC signature"""
    expected_signature = sign_request(payload, secret)
    return hmac.compare_digest(signature, expected_signature)

def create_webhook_headers(payload: Dict[str, Any], secret: str) -> Dict[str, str]:
    """Create headers with HMAC signature for webhook calls"""
    signature = sign_request(payload, secret)
    return {
        'Content-Type': 'application/json',
        'X-Hook-Signature': signature,
        'X-Hook-Timestamp': str(int(time.time())),
        'User-Agent': 'Hospital-POC-Extensions/1.0'
    }

def matches_criteria(data: Dict[str, Any], criteria: Dict[str, Any]) -> bool:
    """Check if data matches the given criteria"""
    for key, expected_value in criteria.items():
        if key not in data:
            return False
        
        # Handle simple equality
        if not isinstance(expected_value, dict):
            if data[key] != expected_value:
                return False
        else:
            # Handle MongoDB-style operators
            for operator, value in expected_value.items():
                if operator == "$lt":
                    if not (data[key] < value):
                        return False
                elif operator == "$lte":
                    if not (data[key] <= value):
                        return False
                elif operator == "$gt":
                    if not (data[key] > value):
                        return False
                elif operator == "$gte":
                    if not (data[key] >= value):
                        return False
                elif operator == "$ne":
                    if not (data[key] != value):
                        return False
                elif operator == "$in":
                    if data[key] not in value:
                        return False
                elif operator == "$nin":
                    if data[key] in value:
                        return False
                else:
                    # Unknown operator, fall back to exact match
                    if data[key] != expected_value:
                        return False
    return True
